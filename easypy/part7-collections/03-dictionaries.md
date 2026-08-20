# Chapter 23: Dictionaries — Labeled Values

A **dictionary** maps **keys** to **values** — like a real dictionary maps words to definitions. Useful for shape names, high scores, and key bindings.

Lists use **numbered slots** (0, 1, 2…). Dictionaries use **labels** you choose — `"I"`, `"Alice"`, `"a"`. When you look up by label, you get the matching value fast. No need to remember that "T-piece" lives at index 4.

## Create and Access

```python
piece_names = {
    "I": "long line",
    "O": "square",
    "T": "T-shape",
}

print(piece_names["T"])  # T-shape
print(piece_names["I"])    # long line
```

Curly braces `{ }` define a dict. Each entry is `key: value`, separated by commas.

## Add and Change

```python
high_scores = {"Alice": 1200, "Bob": 900}
high_scores["You"] = 500
high_scores["Alice"] = 1500

print(high_scores)
# {'Alice': 1500, 'Bob': 900, 'You': 500}
```

Adding a **new key** creates a new entry. Assigning to an **existing key** overwrites the old value — Alice's score updates in place.

## Safe Get

```python
value = high_scores.get("Charlie", 0)
print(value)  # 0

# This would crash:
# print(high_scores["Charlie"])  # KeyError
```

**`.get(key, default)`** returns `default` when the key is missing. Player names and keyboard keys are unpredictable — `get` keeps your game from stopping on a typo.

## Check If a Key Exists

```python
if "Bob" in high_scores:
    print("Bob has a score:", high_scores["Bob"])

if "Charlie" not in high_scores:
    print("Charlie has not played yet")
```

Use `in` before you read a key, or stick with `.get` when a missing key is normal.

## Loop Dictionary

```python
for name, score in high_scores.items():
    print(name, ":", score)
# expected output (order may vary):
# Alice : 1500
# Bob : 900
# You : 500
```

**`.items()`** gives you pairs `(key, value)` one at a time. Great for printing a leaderboard or debugging shape data.

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

Step by step when the player presses a key:

1. Read one character (e.g. `"d"`).
2. Look it up in `CONTROLS`.
3. If found, run the matching action name in your game loop later.
4. If not found, ignore or show help — your choice.

Using a dict means you can change `"a"` to `"left"` in **one place** instead of a long chain of `if/elif`.

## Tetris — Shape Offsets (Preview)

Shapes can be dict keyed by name — we detail in Part 9:

```python
SHAPES = {
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "I": [(0, 0), (0, 1), (0, 2), (0, 3)],
}
```

Each value is a list of `(row, col)` offsets from a piece anchor. The letter `"O"` points at **how to draw** that shape — data and code stay separate.

## Keys Must Be Immutable

Use strings, numbers, tuples as keys — not lists.

```python
# OK:
ok = {("I", 0): "first rotation of I-piece"}

# NOT OK:
# bad = {[1, 2]: "value"}  # TypeError — list is mutable
```

Keys must stay stable. If a key could change behind Python's back, the dict could not find it again. Lists can change; strings and tuples cannot (in the way that matters here).

## Dict vs List — When to Use Which

| Need | Use |
|------|-----|
| Ordered row of 10 cells | **List** |
| Whole 20×10 board | **List of lists** |
| Letter → shape geometry | **Dict** |
| Player name → score | **Dict** |
| Key → game action | **Dict** |

## Common Mistakes

| Mistake | What happens | Fix |
|---------|--------------|-----|
| `dict["missing"]` | `KeyError` | Use `.get(key, default)` |
| Using a list as key | `TypeError` | Use string or tuple |
| Typo in key `"lef"` vs `"left"` | Silent miss — action not found | Centralize keys in `CONTROLS` |
| Forgetting dicts are unordered (older mental model) | Surprise when printing order | Loop with `.items()`; do not rely on order for logic |

## Try It Yourself

Build a dict of 4 Tetris piece letters to English descriptions. Loop and print each.

**Bonus:** Add a dict mapping each letter to a single character for display, e.g. `"I": "I"`, `"O": "O"`, and print a "next piece" preview using `piece_display[name]`.

## Summary

- **dict** `{key: value}` for labeled data.
- **`.get(key, default)`** avoids errors on missing keys.
- **`in`** checks membership; **`.items()`** loops pairs.
- Use for **controls** and **shape definitions**.
- Next: **functions** — organize code.

**Next:** [Why Functions?](../part8-functions/01-why-functions.md)
