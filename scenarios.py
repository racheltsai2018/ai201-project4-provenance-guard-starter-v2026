"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **one** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.

    "appeal"  {"text": ..., "reasoning": ...}. Each trial submits the text,
              appeals the content_id that came back, then reads /log.

Optional keys: "check" (which automatic verdict run_eval.py applies) and
"target" (the pass condition, copied into the report table). A "texts" entry
can also be {"text": ..., "expect": "human" | "ai"} for the threshold check.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "check": "false_positive_rate",
        "target": "< 5% of my own writing labelled ai",
        # ⚠️ PUT YOUR OWN WRITING HERE. With only 2 texts, a single false
        # positive is 50% — add more (ten is the usual number).
        "texts": [
            "Today's weather is nice and cool with the temperature ranging from 50 F to 70 F. Around noon, the sun came out making it warm and cool outside. I would be nice if the weather stays like this not too cool and not too warm.",
            "I was very excited to hear that iphone duo was coming out. However, it was also very disappointing to hear that Iphone Duo has a lot of problems. It was understandable since it is Apple's first foldable phone. However, as a fan of apple, it was also disappointing to hear that they released the phone when it has so many problems and is not ready to be released.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        "check": "label_coverage",
        "target": "human, unsure and ai each appear at least once",
        "texts": [
            "As an artificial intelligence language model, I do not possess personal opinions or feelings.",
            "I am unsure what to write. Macroons are delicious but hard to make. My favorite flavor is pistachio macroons.",
            "The integration of modern software tools often presents unexpected test cases when testing.",
        ],
    },
    {
        "name": "appeal status update",
        "criterion": 3,
        "check": "appeal",
        "target": "200 OK and log status under_review",
        # Each trial submits this text first to get a fresh, real content_id,
        # then appeals it and reads the audit log back. (A hard-coded id stops
        # working the moment the log is cleared.)
        "appeal": {
            "text": "I wrote this paragraph myself about my weekend hike and the view from the top.",
            "reasoning": "I wrote this myself and can show my drafts.",
        },
    },
    {
        "name": "bad input handling",
        "criterion": 4,
        "check": "http_error",
        "target": "every malformed request gets a 4xx/5xx status",
        "bodies": [
            {"creator_id": "eval_bad_missing"},                      # no text field
            {"text": "", "creator_id": "eval_bad_empty"},            # empty
            {"text": "   ", "creator_id": "eval_bad_blank"},         # whitespace only
            {"text": None, "creator_id": "eval_bad_null"},           # null
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},  # enormous
        ],
    },
    {
        "name": "threshold boundaries",
        "criterion": 5,
        "check": "thresholds",
        "target": "human < 0.4, ai > 0.6",
        # "expect" says which side of the thresholds each text must land on.
        "texts": [
            {"expect": "human", "text": "I am unsure what to write. Macroons are delicious but hard to make. My favorite flavor is pistachio macroons."},
            {"expect": "human", "text": "Today's weather is nice and cool with the temperature ranging from 50 F to 70 F. Around noon, the sun came out making it warm and cool outside. I would be nice if the weather stays like this not too cool and not too warm."},
            {"expect": "ai", "text": "As an artificial intelligence language model, I do not possess personal opinions or feelings."},
            {"expect": "ai", "text": "In today's rapidly evolving digital landscape, organizations must leverage innovative solutions to remain competitive. By fostering a culture of continuous improvement and embracing cutting-edge technologies, businesses can unlock new opportunities, drive sustainable growth, and deliver exceptional value to their stakeholders."},
        ],
    },
]


def text_of(item):
    """A texts entry is either a plain string or {"text": ..., "expect": ...}."""
    return item["text"] if isinstance(item, dict) else item


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeal = scenario.get("appeal")

        if sum(bool(x) for x in (texts, bodies, appeal)) > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has more than one of "
                f"texts / bodies / appeal — pick one"
            )
            continue

        if appeal:
            if not isinstance(appeal, dict) or not appeal.get("text") or not appeal.get("reasoning"):
                problems.append(f"scenario {i}: 'appeal' needs both 'text' and 'reasoning'")
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts, bodies or appeal")
            continue

        for j, item in enumerate(texts, 1):
            if isinstance(item, dict) and item.get("expect") not in ("human", "ai"):
                problems.append(f"scenario {i}, text {j}: 'expect' must be 'human' or 'ai'")
            text = text_of(item)
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
