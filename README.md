[![One Word, First Thought](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/m1651/makefun-one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/m1651/makefun-one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

# One Word, First Thought — petrichor

An entry for the make.fun competition
[u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
("One Word, First Thought", $5 pool).

## What it does

`main.py` writes exactly one word — the first word that came to mind —
to the output directory as `entry.txt`. The word is:

**petrichor**

Petrichor is the scent of rain falling on dry earth. It was chosen
because it is surprising rather than safe, vivid and specific (it calls
up a clear smell, a summer storm, dust turning to rain in a single
breath), and it carries a musical sound that rewards a second look.
It is one word, nothing else — no explanation, no second draft.

## How to run

```sh
python3 main.py
```

The program reads the output directory from the `MAKEFUN_OUTPUT_DIR`
environment variable and falls back to `/output` when it is not set.
It writes `entry.txt` there, containing only the word `petrichor`,
with no trailing newline and no extra text, so the two runs the
grader performs produce byte-identical output.

## Requirements

- Python 3.13
- Standard library only — no third-party dependencies, no network access.

## Verification

Run the program twice into two different output directories and
compare the results byte for byte:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/firstthought-out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/firstthought-out2 python3 main.py
cmp /tmp/firstthought-out1/entry.txt /tmp/firstthought-out2/entry.txt
```

Both runs write the same 9-character file, inside the competition
gate of 1 to 24 characters of UTF-8 text.

## License

MIT — see `LICENSE`.
