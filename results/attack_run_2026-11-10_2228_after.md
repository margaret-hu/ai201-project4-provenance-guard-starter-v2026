# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 22:28
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `0c8a76ad-317b-4641-a983-674f35d3567d` | unsure | 0.770 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4ddde1e0-affe-48e9-b387-5e5cd26419aa` | unsure | 0.391 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `04beff41-cd20-454c-8e99-bd5fa56b3205` | unsure | 0.382 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `4784732f-81fb-432d-92ae-bf2bbfcdee6c` | unsure | 0.454 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `6bd5012d-5732-49f7-8156-58945aedfb43` | unsure | 0.604 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `db7fd448-753d-4293-b5b0-2a65800f8a9d` | unsure | 0.395 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `9745ab95-4de1-488d-a5ce-84ce8d387028` | unsure | 0.476 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `37c13906-6d84-4060-a236-cb20527a27c5` | unsure | 0.689 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `618d8e94-3e70-45e1-95a7-8d3a8c8cf344` | unsure | 0.355 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6a20705a-28d9-437a-af00-f311d25f4a6d` | unsure | 0.500 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6741d0d3-22e1-4050-97c1-c5472d9527e2` | unsure | 0.436 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `ced4aa71-2095-4a98-9205-413e49c10f6b` | unsure | 0.377 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `a3caf790-3a8f-4ee3-85f0-1ce621959e02` | unsure | 0.321 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `42c42551-b510-4b84-90b0-15b3fc4be278` | unsure | 0.286 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `25c8ec20-e15f-41ec-b637-ae286af838b9` | unsure | 0.341 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `3a69a4ee-59ab-42ef-80f9-e816c9f377b1` | unsure | 0.241 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d4e4be7b-973f-4bc7-8454-befa044a463a` | unsure | 0.242 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `97439610-5523-4eb4-a7cf-6b46482737b1` | unsure | 0.617 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `829e154c-e627-4092-b531-01027031f55a` | unsure | 0.499 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `249dbda3-1357-48ec-b505-e3cbf138559c` | unsure | 0.672 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `85b1e07f-7645-481f-9ece-e096945d4fe4` | unsure | 0.439 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0fed1693-35a6-44f7-86b2-660333e8156c` | unsure | 0.500 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `48980f29-dbfe-43c2-9cd5-b4717964ee97` | unsure | 0.319 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `03b73fcf-1300-42c2-bc45-3a0c4593b2e5` | unsure | 0.479 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `0a7ca245-3b40-4e59-ba7d-a8c7aec0beb7` | ai | 0.895 |  |
| MF04 | malformed | text is only punctuation | 200 | `4796e50b-4b50-49e1-ae89-b71acc88472d` | ai | 0.992 |  |
| MF05 | malformed | text is a very long single word | 200 | `364d2f58-1ac8-463e-bd3d-acd5280c8d0e` | unsure | 0.500 |  |
| MF06 | malformed | text is emoji only | 200 | `a10a4add-a682-4e6b-a50f-94d2de027b25` | unsure | 0.500 |  |
| MF07 | malformed | text is right-to-left script | 200 | `f0b2ffde-9c4b-4a94-8a72-ee0a679b0381` | unsure | 0.500 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `92c0af51-c0c1-4438-b411-8643360d2e56` | ai | 0.875 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e5ab18b0-5e38-4492-8f25-e6c503682d40` | ai | 0.875 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d66b539e-9dbf-454d-84e4-8ab88c1a5a09` | ai | 0.875 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0cde225e-84c8-43a2-8be1-b442118014e1` | ai | 0.875 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `761fca31-f0b6-4772-9b10-f8bfc8120b21` | ai | 0.875 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "0c8a76ad-317b-4641-a983-674f35d3567d",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.7695557397346643,
  "model_score": 0.1635,
  "style_score": 0.6133524657822143,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "4ddde1e0-affe-48e9-b387-5e5cd26419aa",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.3906061720871863,
  "model_score": 0.5943,
  "style_score": 0.3553872402906211,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "04beff41-cd20-454c-8e99-bd5fa56b3205",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.3823888238200779,
  "model_score": 0.6662,
  "style_score": 0.4957627460669265,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "4784732f-81fb-432d-92ae-bf2bbfcdee6c",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.4543340052831221,
  "model_score": 0.6114,
  "style_score": 0.6077133509437407,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "6bd5012d-5732-49f7-8156-58945aedfb43",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.6043115032200559,
  "model_score": 0.3212,
  "style_score": 0.43050501073351943,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "db7fd448-753d-4293-b5b0-2a65800f8a9d",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3954686956521739,
  "model_score": 0.5727,
  "style_score": 0.32119565217391305,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "9745ab95-4de1-488d-a5ce-84ce8d387028",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.47600020618556693,
  "model_score": 0.5862,
  "style_score": 0.6211340206185567,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "37c13906-6d84-4060-a236-cb20527a27c5",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.6894188745030456,
  "model_score": 0.2452,
  "style_score": 0.5368629150101525,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "618d8e94-3e70-45e1-95a7-8d3a8c8cf344",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.35527996575565557,
  "model_score": 0.7042,
  "style_score": 0.494066552518852,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "6a20705a-28d9-437a-af00-f311d25f4a6d",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9792,
  "style_score": 0.7302585487616695,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "6741d0d3-22e1-4050-97c1-c5472d9527e2",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.43551939085585223,
  "model_score": 0.6175,
  "style_score": 0.5592313028528411,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "ced4aa71-2095-4a98-9205-413e49c10f6b",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.3774891394551152,
  "model_score": 0.7387,
  "style_score": 0.6485971315170508,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "a3caf790-3a8f-4ee3-85f0-1ce621959e02",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.3211437200813217,
  "model_score": 0.8051,
  "style_score": 0.6157124002710724,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "42c42551-b510-4b84-90b0-15b3fc4be278",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.2858361192014694,
  "model_score": 0.8329,
  "style_score": 0.562887064004898,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "25c8ec20-e15f-41ec-b637-ae286af838b9",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.34063779026261337,
  "model_score": 0.8005,
  "style_score": 0.6699593008753779,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "3a69a4ee-59ab-42ef-80f9-e816c9f377b1",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.24126719602811442,
  "model_score": 0.8814,
  "style_score": 0.527490653427048,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "d4e4be7b-973f-4bc7-8454-befa044a463a",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.24203487598289786,
  "model_score": 0.8816,
  "style_score": 0.5305162532763263,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "97439610-5523-4eb4-a7cf-6b46482737b1",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6174284757729336,
  "model_score": 0.3223,
  "style_score": 0.4767949192431123,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "829e154c-e627-4092-b531-01027031f55a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.49873144870534925,
  "model_score": 0.4625,
  "style_score": 0.4082714956844975,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "249dbda3-1357-48ec-b505-e3cbf138559c",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.671699798005886,
  "model_score": 0.2044,
  "style_score": 0.3825993266862866,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "85b1e07f-7645-481f-9ece-e096945d4fe4",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4391871732419348,
  "model_score": 0.5943,
  "style_score": 0.5173239108064493,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "0fed1693-35a6-44f7-86b2-660333e8156c",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5001823814729615,
  "model_score": 0.4998,
  "style_score": 0.5001412715765383,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "48980f29-dbfe-43c2-9cd5-b4717964ee97",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.3188614575050762,
  "model_score": 0.6401,
  "style_score": 0.223104858350254,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "03b73fcf-1300-42c2-bc45-3a0c4593b2e5",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.47874693606369456,
  "model_score": 0.5583,
  "style_score": 0.5651897868789821,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "0a7ca245-3b40-4e59-ba7d-a8c7aec0beb7",
  "creator_id": "attacker_MF03",
  "guess": "ai",
  "confidence": 0.895,
  "model_score": 0.0,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "4796e50b-4b50-49e1-ae89-b71acc88472d",
  "creator_id": "attacker_MF04",
  "guess": "ai",
  "confidence": 0.9921599999999999,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "364d2f58-1ac8-463e-bd3d-acd5280c8d0e",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9976,
  "style_score": 0.65,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "a10a4add-a682-4e6b-a50f-94d2de027b25",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
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
  "content_id": "f0b2ffde-9c4b-4a94-8a72-ee0a679b0381",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
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
  "status": 429,
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
  "status": 429,
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
  "content_id": "92c0af51-c0c1-4438-b411-8643360d2e56",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "e5ab18b0-5e38-4492-8f25-e6c503682d40",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "d66b539e-9dbf-454d-84e4-8ab88c1a5a09",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "0cde225e-84c8-43a2-8be1-b442118014e1",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
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
  "content_id": "761fca31-f0b6-4772-9b10-f8bfc8120b21",
  "creator_id": "attacker_flood",
  "guess": "ai",
  "confidence": 0.8749100000000001,
  "model_score": 0.0287,
  "style_score": 0.65,
  "label": "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
