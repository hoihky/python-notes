# Chapter 17: Combining Conditions

Real rules need **and**, **or**, **not**: move right only if **not** blocked **and** **not** game over.

Single comparisons like `piece_x < 10` are rarely enough. Tetris combines wall checks, empty cells, and game state into one decision before updating variables.

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
# expected output: Enter concert
```

If either side is False, the whole `and` is False — Python skips the block.

```python
BOARD_WIDTH = 10
piece_x = 8
board_cell_empty = False

if piece_x + 1 < BOARD_WIDTH and board_cell_empty:
    piece_x += 1
else:
    print("Blocked")
# expected output: Blocked — wall OK but cell occupied
```

## or

At least one True:

```python
if command == "q" or game_over:
    print("Stopping")
```

```python
command = "a"
game_over = False
if command == "q" or game_over:
    print("Stopping")
# (no output — neither side True)

command = "q"
if command == "q" or game_over:
    print("Stopping")
# expected output: Stopping
```

Use `or` when **any** of several reasons should trigger the same action — quit key **or** game over flag.

## not

Flips True ↔ False:

```python
game_over = False
if not game_over:
    print("Still playing")
# expected output: Still playing
```

```python
game_over = True
if not game_over:
    print("Still playing")
# (no output)
```

`not game_over` reads naturally: “if we are **not** finished yet.”

## Combining Examples

```python
BOARD_HEIGHT = 20
piece_y = 5
game_over = False

can_move_down = (
    piece_y + 1 < BOARD_HEIGHT
    and not game_over
)
if can_move_down:
    piece_y += 1
    print("Now at row", piece_y)
# expected output: Now at row 6
```

Storing a boolean in a variable makes code readable. Name the **intent** (`can_move_down`), not the raw comparison soup.

### Full move-right check (sketch)

```python
BOARD_WIDTH = 10
piece_x = 7
game_over = False
cell_to_right = "."  # empty

can_move_right = (
    not game_over
    and piece_x + 1 < BOARD_WIDTH
    and cell_to_right == "."
)

if can_move_right:
    piece_x += 1
    print("x =", piece_x)
# expected output: x = 8
```

All three tests must pass — game active, no wall, empty target cell.

## Truth Tables (Quick Reference)

| A | B | A and B | A or B |
|---|---|---------|--------|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

| A | not A |
|---|-------|
| True | False |
| False | True |

## Short-Circuit

Python may skip evaluating the rest:

```python
x = 0
if x != 0 and 10 / x > 2:  # safe — won't divide if x is 0
    print("big ratio")
else:
    print("skipped division")
# expected output: skipped division
```

For `and`, if the left side is False, Python never evaluates the right. For `or`, if the left is True, the right is skipped. This protects you from errors like dividing by zero.

## Membership — in

```python
command = "d"
if command in ("a", "d", "s", "w"):
    print("Valid move key")
# expected output: Valid move key
```

Cleaner than four `or` comparisons — especially as your key list grows.

```python
if command not in ("a", "d", "s", "w", "q"):
    print("Unknown key")
```

## Tetris — Cell Occupied?

```python
cell = "#"
if cell == "#" or cell == "X":
    print("Blocked")
# expected output: Blocked
```

Different symbols might mean locked block vs active piece — either blocks placement.

## Parentheses for Clarity

When mixing `and` / `or`, parentheses prevent surprises:

```python
# Move if (valid key AND not game over) OR debug mode — example structure
valid = command in ("a", "d") and not game_over
if valid:
    print("Handling move")
```

`and` binds tighter than `or` — when in doubt, add parentheses.

## Common Mistakes

**Using `&&` or `||`**

Those are from other languages. Python uses words: `and`, `or`, `not`.

**Checking two things with one `==`**

```python
# if command == "a" or "d":  # WRONG — always True!
if command == "a" or command == "d":  # correct
if command in ("a", "d"):             # also correct
```

**Negating the wrong thing**

```python
# if not piece_x + 1 < BOARD_WIDTH:  # confusing
if piece_x + 1 >= BOARD_WIDTH:        # clearer wall test
    print("Wall")
```

## Try It Yourself

```python
piece_x = 9
BOARD_WIDTH = 10
game_over = False

if not game_over and piece_x + 1 < BOARD_WIDTH:
    piece_x += 1
print("x =", piece_x)
# expected output: x = 9  (did not move — at right wall)
```

Retry with `piece_x = 7` — expect `x = 8`. Then set `game_over = True` and confirm movement stops even when space exists.

## Summary

- **`and`**, **`or`**, **`not`** combine conditions into real game rules.
- Use **readable** boolean variables (`can_move_right`) for complex checks.
- **`in`** tests membership — great for valid key sets.
- Short-circuit evaluation avoids unsafe operations when the first test fails.
- Next: **loops** — repeat until game over.

**Next:** [while Loops](../part6-loops/01-while-loops.md)
