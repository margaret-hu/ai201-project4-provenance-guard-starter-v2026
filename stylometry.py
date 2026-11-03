"""
Signal two: the style signal.

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
    How much sentence length varies.

    Returns:
        A float >= 0: the coefficient of variation of sentence lengths (in
        words), i.e. stdev / mean, so long and short texts are comparable.
        It has no fixed upper bound; typical prose falls roughly in 0–1.
        HIGHER means lumpier sentences, which reads as MORE HUMAN. LOWER means
        evenly sized sentences, which reads as MORE AI-LIKE, so `style_signal`
        must flip it before combining.

    Fewer than two sentences returns 0.0, which leans AI-ish: a known bias for
    very short inputs.
    """
    lengths = [len(words(s)) for s in sentences(text)]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    return statistics.stdev(lengths) / mean_length


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary, which
        reads as MORE HUMAN. Lower means more repetition, which reads as MORE
        AI-LIKE, so `style_signal` must flip it before combining. Empty text
        returns 0.0.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    tokens = words(text)

    if not tokens:
        return 0.0
    
    return len(set(tokens)) / len(tokens)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float >= 0: punctuation characters per word. Full stops, apostrophes
        and hyphens are not counted, so abbreviations, contractions and
        "well-known" don't inflate it. Empty text returns 0.0.

        Direction is not settled: the Milestone 4 test pieces barely differ on
        it, so `style_signal` treats low density as AI-like but weights it
        lowest.
    """
    punctuation = ",;:!?()—–…\"“”"
    tokens = words(text)

    if not tokens:
        return 0.0

    punctuation_count = sum(1 for ch in text if ch in punctuation)

    return punctuation_count / len(tokens)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    A weighted average of the three measures, each flipped and scaled to 0–1
    so it points the same way as `detector.model_signal`.

    Known weakness: on the Milestone 4 test pieces this score does not
    separate AI from human (the clearly-AI piece scored lowest). Treat it as a
    weak signal, not evidence on its own.
    """
    # Each measure is put on 0–1 with higher = more AI-like, then averaged.
    spread_ai = 1 - min(sentence_length_spread(text), 1.0)
    ttr_ai = 1 - type_token_ratio(text)
    punctuation_ai = 1 - min(punctuation_density(text), 0.5) / 0.5

    # Weights sum to 1: 0.4 spread, 0.35 type-token ratio, 0.25 punctuation.
    # Punctuation is lowest because its direction is the least certain.
    return 0.4 * spread_ai + 0.35 * ttr_ai + 0.25 * punctuation_ai


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
