---
title: Dictionaries — Labeled Values
order: 3
---

# Chapter 23: Dictionaries — Labeled Values

A **dictionary** maps **keys** to **values** — like a real dictionary maps words to definitions. Useful for shape names, high scores, and key bindings.

## Create and Access

```python
piece_names = {
    "I": "long line",
    "O": "square",
    "T": "T-shape",
}

print(piece_names["T"])
```

## Add and Change

```python
high_scores = {"Alice": 1200, "Bob": 900}
high_scores["You"] = 500
high_scores["Alice"] = 1500
```

## Safe Get

```python
value = high_scores.get("Charlie", 0)  # 0 if missing
```

## Loop Dictionary

```python
for name, score in high_scores.items():
    print(name, score)
```

## Tetris — Key Bindings

```python
CONTROLS = {
    "a": "left",
    "d": "right",
    "s": "soft_drop",
    "w": "rotate",
    "q": "quit",
}

cmd = input("Key: ")
action = CONTROLS.get(cmd)
if action:
    print("Do:", action)
else:
    print("Unknown key")
```

## Tetris — Shape Offsets (Preview)

Shapes can be dict keyed by name — we detail in Part 9:

```python
SHAPES = {
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
}
```

Each value is list of `(row, col)` offsets from piece anchor.

## Keys Must Be Immutable

Use strings, numbers, tuples as keys — not lists.

## Try It Yourself

Build a dict of 4 Tetris piece letters to English descriptions. Loop and print each.

## Summary

- **dict** `{key: value}` for labeled data.
- **`.get(key, default)`** avoids errors on missing keys.
- Use for **controls** and **shape definitions**.
- Next: **functions** — organize code.

**Next:** [Why Functions?](../part8-functions/01-why-functions.html)
