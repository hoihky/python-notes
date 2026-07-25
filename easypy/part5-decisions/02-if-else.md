---
title: if and else
order: 2
---

# Chapter 16: if and else

**if** lets Python **choose** which code runs. Without it, Tetris could not check walls or clear lines.

## Basic if

```python
score = 1500
if score >= 1000:
    print("Great job!")
```

Structure:

```python
if condition:
    indented_line
    another_indented_line
```

- **Colon** `:` after condition
- **Indented** block (4 spaces — VS Code helps)

If `condition` is **False**, Python **skips** the block.

## else

```python
command = input("Move (a/d): ")
if command == "a":
    print("Moving left")
else:
    print("Not left")
```

## elif — Multiple Choices

```python
command = input("Move: ")
if command == "a":
    print("Left")
elif command == "d":
    print("Right")
elif command == "s":
    print("Down")
else:
    print("Unknown")
```

Tetris command handler will look like this.

## Nested if

```python
if not game_over:
    if piece_x < BOARD_WIDTH - 1:
        piece_x += 1
```

## Tetris — Wall Check

```python
BOARD_WIDTH = 10
piece_x = 8

if piece_x + 1 < BOARD_WIDTH:
    piece_x += 1
    print("Moved right to", piece_x)
else:
    print("Blocked by wall")
```

## Tetris — Game Over Check

```python
if piece_y <= 0:
    game_over = True
    print("Game Over!")
```

(Exact rules refined when we build the board.)

## Indentation Errors

```python
if True:
print("wrong")  # IndentationError
```

Always indent the block under `if`.

## Try It Yourself

```python
lines = int(input("Lines cleared this turn: "))
if lines == 0:
    print("Keep going!")
elif lines == 1:
    print("Single!")
elif lines >= 4:
    print("TETRIS!")
else:
    print("Nice combo!")
```

## Summary

- **`if`** runs code only when condition is True.
- **`else`** / **`elif`** handle other cases.
- **Indentation** defines blocks.
- Tetris uses `if` for movement, collision, game over.

**Next:** [Combining Conditions](03-combining-conditions.html)
