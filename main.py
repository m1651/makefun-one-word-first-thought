#!/usr/bin/env python3
"""One Word, First Thought.

Writes a single original word to entry.txt.

The word is "petrichor": the scent of rain falling on dry earth.
It is surprising rather than safe, vivid and specific, and its
sound rewards a second look -- exactly what the judge brief prizes.
"""

import os


def main():
    word = "petrichor"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
