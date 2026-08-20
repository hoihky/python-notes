# Chapter 15: True, False, and Comparisons

Programs must **decide**: Is the cell empty? Is the game over? Decisions use **boolean** values — **True** or **False**.

A boolean is not a number and not text — it is an answer to a yes-or-no question. Tetris asks dozens of these every frame: wall? floor? filled cell? line complete?

## Booleans

```python
game_over = False
cell_filled = True
print(type(True))   # expected output: <class 'bool'>
print(type(False))  # expected output: <class 'bool'>
```

Only two values: `True`, `False` (capital T and F). Lowercase `true` or `false` will cause a **NameError** — Python treats them as undefined names, not booleans.

You can assign booleans directly or compute them with comparisons:

```python
can_rotate = True
hit_bottom = False
print(can_rotate, hit_bottom)  # expected output: True False
```

## Comparison Operators

Compare two values — result is True or False:

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal | `5 == 5` → True |
| `!=` | not equal | `5 != 3` → True |
| `<` | less than | `3 < 5` → True |
| `>` | greater than | `3 > 5` → False |
| `<=` | less or equal | `5 <= 5` → True |
| `>=` | greater or equal | `4 >= 5` → False |

```python
piece_x = 4
print(piece_x == 4)   # expected output: True
print(piece_x < 10)   # expected output: True
print(piece_x == 5)   # expected output: False
```

**Warning:** `=` assigns; `==` compares. This is one of the most common beginner mix-ups:

```python
x = 5      # stores 5 in x
x == 5     # asks: does x equal 5? → True
```

## Strings Compare Too

```python
shape = "I"
print(shape == "I")   # expected output: True
print(shape == "O")   # expected output: False
print(shape != "T")   # expected output: True
```

Comparisons are case-sensitive: `"i" == "I"` is **False**.

## Tetris Questions as Booleans

```python
BOARD_WIDTH = 10
piece_x = 9
can_move_right = piece_x + 1 < BOARD_WIDTH
print(can_move_right)  # expected output: False — would hit wall
```

Column indices run `0` through `9` on a width-10 board. At `piece_x == 9`, the next column would be `10`, which is outside the board — so `can_move_right` is **False**.

```python
cell = "."
is_empty = (cell == ".")
print(is_empty)  # expected output: True
```

Empty cells might be drawn as `.`; locked blocks as `#`. Comparing the character tells you whether a move is allowed.

### More Tetris-style checks

```python
BOARD_HEIGHT = 20
piece_y = 0
at_top_row = (piece_y == 0)
print(at_top_row)  # expected output: True

locked_cell = "#"
is_blocked = (locked_cell != ".")
print(is_blocked)  # expected output: True
```

## Storing Test Results

```python
BOARD_WIDTH = 10
piece_x = 9
hit_wall = piece_x >= BOARD_WIDTH - 1
print(hit_wall)  # expected output: True

if hit_wall:
    print("Cannot go right")
# expected output: Cannot go right
```

(`if` fully explained next chapter.) Storing the comparison in `hit_wall` keeps the `if` line short and gives the idea a name you can reuse.

## Chaining Comparisons (Python Bonus)

Python allows readable range checks:

```python
piece_x = 4
in_bounds = 0 <= piece_x < BOARD_WIDTH  # set BOARD_WIDTH = 10
print(in_bounds)  # expected output: True
```

Same as `piece_x >= 0 and piece_x < BOARD_WIDTH`, but closer to how you think: “column 4 is inside 0..9.”

## None — “No Value Yet”

```python
current_piece = None
print(current_piece is None)  # expected output: True
```

Means “nothing assigned yet” — useful before spawning a piece at game start. `None` is its own type; do not confuse it with `False` or `0`.

## Truthiness Preview

Later you will see `if score:` — for now, know that `0`, empty strings, and `None` act like **False** in conditions; most other values act like **True**. Explicit comparisons (`score > 0`) stay clearest while learning.

## Common Mistakes

**Using `=` inside a condition**

```python
# if piece_x = 4:  # SyntaxError
if piece_x == 4:
    print("Spawn column")
```

**Comparing floats with `==`**

```python
# 0.1 + 0.2 == 0.3  # False — floating-point quirk; rare in grid Tetris
```

Stick to integers for board coordinates and you avoid this.

**Off-by-one on walls**

```python
BOARD_WIDTH = 10
# Last valid column is 9, not 10
print(9 < BOARD_WIDTH)   # True — can stand in column 9
print(10 < BOARD_WIDTH)  # False — column 10 is out of bounds
```

## Try It Yourself

```python
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
piece_x = 0
piece_y = 19

print("On bottom?", piece_y >= BOARD_HEIGHT - 1)
# expected output: On bottom? True

print("Column 0?", piece_x == 0)
# expected output: Column 0? True

piece_x = 9
print("Can move right?", piece_x + 1 < BOARD_WIDTH)
# expected output: Can move right? False
```

Add checks for `piece_y == 0` (top row) and `piece_x == BOARD_WIDTH - 1` (right edge).

## Summary

- **bool**: `True` / `False` — answers to yes/no questions.
- **`==`, `!=`, `<`, `>`** compare values; result is always a boolean.
- **`=` assigns; `==` compares** — keep them separate.
- Tetris logic asks: empty? wall? line full? Store answers in named booleans for clarity.
- Next: **`if` and `else`**.

**Next:** [if and else](02-if-else.md)
