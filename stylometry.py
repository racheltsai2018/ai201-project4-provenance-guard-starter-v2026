"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    # Coefficient of variation: stdev / mean of words-per-sentence.
    # Scale: 0 = every sentence the same length; ~0.2-0.3 is typical of
    # generated prose, ~0.5+ is typical of human writing. HIGHER = more human.
    # Fewer than two sentences has no spread to measure, so return 0.0 and let
    # style_signal treat that case as "no evidence" rather than "very AI".
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    # Moving-average TTR: the plain ratio over every 50-word window, averaged.
    # This keeps a 500-word essay comparable to a 60-word paragraph, which raw
    # TTR does not. Texts shorter than one window fall back to plain TTR.
    # HIGHER = more varied vocabulary = more human.
    toks = words(text)
    if not toks:
        return 0.0
    window = 50
    if len(toks) <= window:
        return len(set(toks)) / len(toks)
    ratios = [
        len(set(toks[i:i + window])) / window
        for i in range(len(toks) - window + 1)
    ]
    return statistics.mean(ratios)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    # Punctuation marks per word, NOT counting full stops (every text has
    # those, so they say little). Commas, semicolons, colons, dashes, brackets,
    # quotes, ! and ? all count. HIGHER = busier, more varied punctuation,
    # which we treat as more human.
    toks = words(text)
    if not toks:
        return 0.0
    marks = re.findall(r"[,;:!?()\"—–…]|--| - ", text)
    return len(marks) / len(toks)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # Each measure runs "higher = more human", so each gets flipped into an
    # AI-ness score between 0 and 1 with a clamped straight line:
    #   at or below the `ai` value  -> 1.0 (looks AI)
    #   at or above the `human` value -> 0.0 (looks human)
    # The anchor values are starting guesses; tune them on your calibration
    # inputs.
    def ai_ness(value: float, ai: float, human: float) -> float:
        return max(0.0, min(1.0, (human - value) / (human - ai)))

    spread_score = ai_ness(sentence_length_spread(text), ai=0.20, human=0.60)
    ttr_score = ai_ness(type_token_ratio(text), ai=0.65, human=0.85)
    punct_score = ai_ness(punctuation_density(text), ai=0.05, human=0.18)

    # One sentence gives no spread evidence: call it neutral, not AI.
    if len(sentences(text)) < 2:
        spread_score = 0.5

    # Spread is the strongest of the three, so it gets the most weight.
    return round(0.45 * spread_score + 0.30 * ttr_score + 0.25 * punct_score, 3)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
