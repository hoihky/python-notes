---
title: True, False, and Comparisons
order: 1
---

# Chapter 15: True, False, and Comparisons

Programs must **decide**: Is the cell empty? Is the game over? Decisions use **boolean** values — **True** or **False**.

## Booleans

```python
game_over = False
cell_filled = True
print(type(True))  # <class 'bool'>
```

Only two values: `True`, `False` (capital T and F).

## Comparison Operators

Compare two values — result is True or False:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal | `5 == 5` → True |
| `!=` | not equal | `5 != 3` → True |
| `<` | less than | `3 < 5` → True |
| `>` | greater than | `3 > 5` → False |
| `<=` | less or equal | |
| `>=` | greater or equal | |

```python
piece_x = 4
print(piece_x == 4)   # True
print(piece_x < 10)   # True
```

**Warning:** `=` assigns; `==` compares.

## Tetris Questions as Booleans

```python
BOARD_WIDTH = 10
piece_x = 9
can_move_right = piece_x + 1 < BOARD_WIDTH
print(can_move_right)  # False — would hit wall
```

```python
cell = "."
is_empty = (cell == ".")
```

## Storing Test Results

```python
hit_wall = piece_x >= BOARD_WIDTH - 1
if hit_wall:
    print("Cannot go right")
```

(`if` fully explained next chapter.)

## None — “No Value Yet”

```python
current_piece = None
```

Means “nothing assigned” — useful before spawning a piece.

## Try It Yourself

```python
BOARD_HEIGHT = 20
piece_y = 19
print("On bottom?", piece_y >= BOARD_HEIGHT - 1)
print("Column 0?", piece_x == 0)  # set piece_x first
```

## Summary

- **bool**: `True` / `False`.
- **`==`, `!=`, `<`, `>`** compare values.
- Tetris logic asks: empty? wall? line full?
- Next: **`if` and `else`**.

**Next:** [if and else](02-if-else.html)
