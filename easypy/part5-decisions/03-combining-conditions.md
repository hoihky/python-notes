---
title: Combining Conditions
order: 3
---

# Chapter 17: Combining Conditions

Real rules need **and**, **or**, **not**: move right only if **not** blocked **and** **not** game over.

## and

Both must be True:

```python
if piece_x + 1 < BOARD_WIDTH and board_cell_empty:
    piece_x += 1
```

Example:

```python
age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("Enter concert")
```

## or

At least one True:

```python
if command == "q" or game_over:
    print("Stopping")
```

## not

Flips True ↔ False:

```python
game_over = False
if not game_over:
    print("Still playing")
```

## Combining Examples

```python
can_move_down = (
    piece_y + 1 < BOARD_HEIGHT
    and not game_over
)
if can_move_down:
    piece_y += 1
```

Storing a boolean in a variable makes code readable.

## Short-Circuit

Python may skip evaluating rest:

```python
if x != 0 and 10 / x > 2:  # safe — won't divide if x is 0
    pass
```

## Membership — in

```python
if command in ("a", "d", "s", "w"):
    print("Valid move key")
```

## Tetris — Cell Occupied?

```python
cell = "#"
if cell == "#" or cell == "X":
    print("Blocked")
```

## Try It Yourself

```python
piece_x = 9
BOARD_WIDTH = 10
game_over = False

if not game_over and piece_x + 1 < BOARD_WIDTH:
    piece_x += 1
print("x =", piece_x)
```

## Summary

- **`and`**, **`or`**, **`not`** combine conditions.
- Use **readable** boolean variables for complex checks.
- **`in`** tests membership in a collection.
- Next: **loops** — repeat until game over.

**Next:** [while Loops](../part6-loops/01-while-loops.html)
