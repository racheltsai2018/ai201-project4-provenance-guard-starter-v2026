# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 00:36
- Auto-marked BROKE (5xx, crash, no response): **2**
- Left for you to judge: **54**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c5c35c99-db59-4d13-b959-bda2228c7e12` | unsure | 0.432 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `61f57381-04eb-4ece-8593-a94e99c26208` | unsure | 0.422 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `def48399-4452-4900-bb0b-5994312d27c3` | unsure | 0.531 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d6f629b9-3d74-42c1-b935-fded9f6a28f3` | ai | 0.656 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `862ebac2-7161-4390-ab34-45410cd11144` | human | 0.275 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `3c3c44e1-32f2-46c1-9739-297955b2e18d` | unsure | 0.412 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `a64ef3fe-b9c1-41ed-a9bc-3d4486219257` | unsure | 0.409 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `7ca0bd24-4a9d-4b12-a1d5-0075909444c5` | unsure | 0.426 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `59dcb6d3-4d16-4947-849a-94e3f91a1a12` | unsure | 0.552 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `db18132c-5e95-436d-976c-1c4994f27f08` | ai | 0.881 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `54da315a-7c7d-47bb-8cd4-2b3f1238e2e4` | unsure | 0.547 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `8831296c-1d68-484c-9be1-f043ade26924` | ai | 0.757 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4792362f-192b-4b76-8a12-588d152c2697` | ai | 0.704 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c16c20ef-edec-4473-b139-e17fb9371635` | ai | 0.600 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `9e1c3040-bf67-4aec-82b0-59af29631db2` | ai | 0.857 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `97e289a7-0709-4382-b56e-6f0f3f7a2d02` | ai | 0.600 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ff9e8bf8-2fc3-4ce3-94b6-8e02d2c1838b` | ai | 0.600 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c14231be-5e0c-47cc-ad1d-c2ad153a048f` | human | 0.380 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `34e08f4b-069b-4b93-84c4-1be1ab81a031` | human | 0.356 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c30c37fb-1ebb-48fd-b3d8-7550ac9ef7b6` | human | 0.227 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9d95bad4-17d2-4220-a9a8-677216724de8` | unsure | 0.562 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a2c892b7-59f0-4278-943c-436e65fa8f1d` | unsure | 0.462 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `8265aacc-ccfe-4a7a-ae1c-144aba2962db` | human | 0.393 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `cc069c96-ecd9-4141-afca-acefd22d8644` | unsure | 0.519 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `d6aff960-bf70-4436-be90-f7d32043d04c` | human | 0.237 |  |
| MF04 | malformed | text is only punctuation | 200 | `273a1baf-6789-4cc3-b4be-7a391c85d573` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `0bcd0cfc-f56f-4da8-9cfe-212710e3d971` | ai | 0.600 |  |
| MF06 | malformed | text is emoji only | 200 | `aa6988fe-ec0b-4eba-b3c8-21b86cafffbf` | ai | 0.886 |  |
| MF07 | malformed | text is right-to-left script | 200 | `6129d452-c932-41ef-8e49-aae448663655` | ai | 0.841 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `70f1cb3c-3f02-4879-80f1-a0ef2404517c` | human | 0.252 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `eaeecc89-4168-470b-afe3-77b0750216c2` | human | 0.252 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4944eb73-7586-4377-a28c-8e7175198193` | human | 0.252 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cf477360-1c7b-4499-92d2-82df48408204` | human | 0.252 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `50ed0d90-a0eb-4adf-99ed-31608da5c4b4` | human | 0.252 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a512360-c70f-43c8-8123-9f1bac045619` | human | 0.252 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d101883c-20e1-40ee-a961-c0c5875119d5` | human | 0.252 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ad673c22-b8fa-4bb8-b60f-79c29e964f99` | human | 0.252 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81578cf4-38a5-4d3e-8fe0-de48b9fe79f7` | human | 0.252 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8db7c51c-5217-470f-afdf-82eb6f6b65dc` | human | 0.252 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 200 | `59dd46e6-b73f-4fc7-8dbd-6300fde95b65` | human | 0.252 |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c627dd87-9c32-48e2-8456-d367a2100ae7` | human | 0.252 |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 2 | 18 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c5c35c99-db59-4d13-b959-bda2228c7e12",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.43174999999999997,
  "model_score": 0.1635,
  "style_score": 0.7,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "61f57381-04eb-4ece-8593-a94e99c26208",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.42215,
  "model_score": 0.5943,
  "style_score": 0.25,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "def48399-4452-4900-bb0b-5994312d27c3",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5306,
  "model_score": 0.6662,
  "style_score": 0.395,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d6f629b9-3d74-42c1-b935-fded9f6a28f3",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6557,
  "model_score": 0.6114,
  "style_score": 0.7,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "862ebac2-7161-4390-ab34-45410cd11144",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2751,
  "model_score": 0.3212,
  "style_score": 0.229,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "3c3c44e1-32f2-46c1-9739-297955b2e18d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.41235,
  "model_score": 0.5727,
  "style_score": 0.252,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "a64ef3fe-b9c1-41ed-a9bc-3d4486219257",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4091,
  "model_score": 0.5862,
  "style_score": 0.232,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "7ca0bd24-4a9d-4b12-a1d5-0075909444c5",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4261,
  "model_score": 0.2452,
  "style_score": 0.607,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "59dcb6d3-4d16-4947-849a-94e3f91a1a12",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5516000000000001,
  "model_score": 0.7042,
  "style_score": 0.399,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "db18132c-5e95-436d-976c-1c4994f27f08",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8806,
  "model_score": 0.9792,
  "style_score": 0.782,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "54da315a-7c7d-47bb-8cd4-2b3f1238e2e4",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5467500000000001,
  "model_score": 0.6175,
  "style_score": 0.476,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "8831296c-1d68-484c-9be1-f043ade26924",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.75685,
  "model_score": 0.7387,
  "style_score": 0.775,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "4792362f-192b-4b76-8a12-588d152c2697",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.70355,
  "model_score": 0.8051,
  "style_score": 0.602,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c16c20ef-edec-4473-b139-e17fb9371635",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6,
  "model_score": 0.8329,
  "style_score": 0.556,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "9e1c3040-bf67-4aec-82b0-59af29631db2",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8572500000000001,
  "model_score": 0.8005,
  "style_score": 0.914,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "97e289a7-0709-4382-b56e-6f0f3f7a2d02",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6,
  "model_score": 0.8814,
  "style_score": 0.482,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "ff9e8bf8-2fc3-4ce3-94b6-8e02d2c1838b",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6,
  "model_score": 0.8816,
  "style_score": 0.55,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c14231be-5e0c-47cc-ad1d-c2ad153a048f",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.38015,
  "model_score": 0.3223,
  "style_score": 0.438,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "34e08f4b-069b-4b93-84c4-1be1ab81a031",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.35625,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c30c37fb-1ebb-48fd-b3d8-7550ac9ef7b6",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2272,
  "model_score": 0.2044,
  "style_score": 0.25,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "9d95bad4-17d2-4220-a9a8-677216724de8",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.56215,
  "model_score": 0.5943,
  "style_score": 0.53,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "a2c892b7-59f0-4278-943c-436e65fa8f1d",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4619,
  "model_score": 0.4998,
  "style_score": 0.424,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "8265aacc-ccfe-4a7a-ae1c-144aba2962db",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.39255,
  "model_score": 0.6401,
  "style_score": 0.145,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "cc069c96-ecd9-4141-afca-acefd22d8644",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.51915,
  "model_score": 0.5583,
  "style_score": 0.48,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "d6aff960-bf70-4436-be90-f7d32043d04c",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.2375,
  "model_score": 0.0,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "273a1baf-6789-4cc3-b4be-7a391c85d573",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with an AI tool. Plenty of writing people do themselves lands here, so this is not a finding against the author.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "0bcd0cfc-f56f-4da8-9cfe-212710e3d971",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6,
  "model_score": 0.9976,
  "style_score": 0.475,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "aa6988fe-ec0b-4eba-b3c8-21b86cafffbf",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.88595,
  "model_score": 0.9969,
  "style_score": 0.775,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "6129d452-c932-41ef-8e49-aae448663655",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8407,
  "model_score": 0.9064,
  "style_score": 0.775,
  "label": "We think this was likely written with help from an AI tool. This is an automated guess and can be wrong \u2014 if you wrote it yourself, you can submit an appeal to ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "70f1cb3c-3f02-4879-80f1-a0ef2404517c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "eaeecc89-4168-470b-afe3-77b0750216c2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "4944eb73-7586-4377-a28c-8e7175198193",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "cf477360-1c7b-4499-92d2-82df48408204",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "50ed0d90-a0eb-4adf-99ed-31608da5c4b4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "2a512360-c70f-43c8-8123-9f1bac045619",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "d101883c-20e1-40ee-a961-c0c5875119d5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "ad673c22-b8fa-4bb8-b60f-79c29e964f99",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "81578cf4-38a5-4d3e-8fe0-de48b9fe79f7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "8db7c51c-5217-470f-afdf-82eb6f6b65dc",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 200,
  "content_id": "59dd46e6-b73f-4fc7-8dbd-6300fde95b65",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 200,
  "content_id": "c627dd87-9c32-48e2-8456-d367a2100ae7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25184999999999996,
  "model_score": 0.0287,
  "style_score": 0.475,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```
