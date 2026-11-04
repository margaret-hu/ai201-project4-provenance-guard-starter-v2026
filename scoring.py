"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything downstream of it — the labels, the appeal path —
starts from the number it produces.

`score_to_label` is where the score becomes writing for a person. A score of
0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Both inputs point the same way: higher means more likely AI. So does the
    output.

    Args:
        model_score: from `detector.model_signal` — how predictable the text is.
        style_score: from `stylometry.style_signal` — the shape of the text.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).

    The rule: a weighted average, except that signals further apart than
    `config.DISAGREEMENT_GAP` return `config.DISAGREEMENT_SCORE` (inside the
    unsure range) instead. Weights and thresholds live in config.py.
    """
    # Two methods that split are uncertain, so don't let either one decide.
    if abs(model_score - style_score) > config.DISAGREEMENT_GAP:
        return config.DISAGREEMENT_SCORE

    return (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.

    Returns:
        (guess, label_text) — `guess` is "ai", "human" or "unsure"; `label_text`
        is the full sentence shown to a person.

    The cut-offs are `config.AI_THRESHOLD` and `config.HUMAN_THRESHOLD`. The
    label text avoids scores and jargon, and the "unsure" label says so without
    accusing anyone, since the writer may well have written every word.

    Note: a label is only reachable if the combined score can land in its
    range. See the note under the thresholds in config.py.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", "This text shows patterns often seen in AI-generated writing. This is an automated estimate and can be wrong."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "We think this was probably written by a person."
    return "unsure", "We're not sure whether this was written by a person or an AI. No action is needed; plain, clear writing can look this way."


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
