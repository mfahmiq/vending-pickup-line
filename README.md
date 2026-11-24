# The Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/mfahmiq/vending-pickup-line/rank.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/mfahmiq/vending-pickup-line/reward.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A single pickup line for the [One Line, One Minute: The Vending Machine Pickup Line Contest](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) on make.fun — written as if a vending machine were flirting with a passing human.

> Hey, you've walked past me 47 times and my coils never tangled like this — drop in a coin and I'll jam on purpose just to keep you here.

One line, 136 characters, spoken by the machine itself. `main.py` writes it to `entry.txt`.

## Why this line is funny

The joke works because it never leaves the machine's world — every beat is something only a vending machine could say:

- **"You've walked past me 47 times"** — the machine has been standing in the same corner, watching, counting. That is exactly what a vending machine does all day: it notices foot traffic. The oddly specific number makes it feel like a real log entry, not a generic compliment.
- **"my coils never tangled like this"** — the coils are the spirals that hold the snacks. "Tangled" is the machine's version of butterflies in the stomach: its insides are literally getting knotted up. A stranger in a bar could never say this; only a machine with coils can.
- **"drop in a coin"** — the machine turns flirting into its own transaction. It is not asking for a phone number; it is asking for the one thing it is built to receive.
- **"I'll jam on purpose just to keep you here"** — the punchline lands on the last few words. A jammed vending machine is every human's most annoying experience, and here the machine confesses it would *choose* to malfunction — the one failure it is famous for, weaponised as devotion. It would rather break itself than let you walk away. That is charming instead of creepy: the machine is the one making the sacrifice, and the "crime" is keeping you near a snack machine for a few extra seconds.

The line is short enough to read in one breath, needs no picture or caption, and the turn arrives at the very end, exactly where the judge's brief wants it.

## How it works

`main.py` is deterministic and uses only the Python standard library. It holds the entry as a single string constant, `ENTRY`, and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

Before writing, it self-verifies the entry against the competition's gate:

- valid UTF-8 text,
- 1–200 characters long,
- a single line (no `\n` or `\r`),
- not whitespace-only.

Any failure exits non-zero and writes nothing.

## Usage

```sh
python3 main.py
# writes /output/entry.txt (136 chars)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt instead
```

Then check the result:

```sh
cat /output/entry.txt
python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
# 136
```

## Files

- `main.py` — the entry program (entrypoint).
- `entry.txt` — the exact entry line, byte-identical to what `main.py` produces.
- `README.md` — this file.
- `LICENSE` — MIT License.
