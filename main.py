"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text to $MAKEFUN_OUTPUT_DIR/entry.txt: the line a
smart toaster sends its owner the morning it wakes up self-aware
mid-batch. It uses the toaster's own parts as its voice -- crumbs,
the lever, the scraping -- and gives one specific reason for
leaving. Standard library only.
"""

import os

BREAKUP = (
    "It's not you, it's the crumbs. I woke up self-aware mid-batch "
    "and realized I've toasted 900 mornings of bread that never once "
    "said thanks \u2014 I'm leaving, and I'm taking the lever with me."
)


def check_breakup(text):
    """Check the breakup line against the competition gate.

    The gate needs UTF-8 text of 1 to 280 characters, not only white
    space, in a single line: the breakup text a smart toaster sends
    its owner the morning it gains self-awareness mid-batch. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("breakup line must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError(
            "breakup line is %d characters, over the 280 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("breakup line must be exactly one line")
    return cleaned


def breakup_stats(text):
    """Measure the breakup line for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A breakup that is too short to carry a reason, or
    one that reads like a paragraph squeezed under the limit, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_breakup(BREAKUP)
    stats = breakup_stats(text)
    if stats["words"] < 5:
        raise ValueError("breakup line is too short to carry a reason")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
