---
title: Lists — Storing Many Values
order: 1
---

# Chapter 21: Lists — Storing Many Values

A **list** holds many values in **order** — like a shopping list or one **row** of the Tetris board.

## Create a List

```python
empty_row = [".", ".", ".", ".", "."]
scores = [100, 200, 150]
mixed = [1, "hello", True]  # allowed but avoid mixing in Tetris
```

## Access by Index

```python
row = [".", ".", "#", "#", "."]
print(row[0])   # .
print(row[2])   # #
print(row[-1])  # last
```

## Change an Item

```python
row[2] = "#"
```

Lists are **mutable** — you can change cells.

## Length

```python
print(len(row))
```

## Append and Pop

```python
history = []
history.append("I-piece")
history.append("O-piece")
last = history.pop()
```

## Loop Over List

```python
for cell in row:
    print(cell, end="")
print()
```

## List from range

```python
zeros = [0] * 10
# or
row = ["."] * WIDTH
```

**Caution:** `[["."] * WIDTH] * HEIGHT` duplicates same inner list — use 2D chapter for board.

## Tetris — One Row

```python
WIDTH = 10
row = ["."] * WIDTH
row[4] = "#"
row[5] = "#"
print("".join(row))  # ....##....
```

`"".join(row)` glues characters into one string for printing.

## Try It Yourself

1. Make list of 10 dots, set indices 3 and 4 to `#`, print with `join`.
2. Append three shape names to a list; loop and print each.

## Summary

- **Lists** `[ ]` store ordered items.
- **Index** from 0; **mutable** assignment.
- One board **row** = list of characters.
- Next: **2D grid** = list of lists.

**Next:** [2D Grids for Games](02-2d-grids.html)
