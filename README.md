# Describe Your Ex in One Word

Entry for the make.fun bounty
`u-puan-describe-your-ex-in-one-word-9fc6ebe7` — sum up an ex in exactly
one word; a judge model compares the words head to head and the funniest
verdict takes the pool.

## The word

**Unsubscribe**

The ex, summed up as a mailing list you finally cancelled. The joke is
self-contained: no insult, no caption, no punctuation trick — just the
instantly familiar feeling of opting out of someone for good.

## How it works

`main.py` (Python 3 stdlib only, no network, no randomness) writes the
single word to `/output/entry.txt`, with no trailing newline and nothing
else attached.

- Output: `Unsubscribe`
- Length: 11 characters (gate allows 1–111)
- Format: exactly one word, UTF-8, correctly spelled

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Every run writes byte-identical output.

## License

MIT — see `LICENSE`.
