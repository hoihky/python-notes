---
title: Naming and Assignment
order: 2
---

# Chapter 13: Naming and Assignment

Good names and clear assignment make code you can read **months later**. Bad names make Tetris feel impossible to fix.

## Naming Rules (Python)

| Rule | Example |
|------|---------|
| Letters, numbers, underscore | `piece_x2` OK |
| Cannot **start** with digit | `2piece` illegal |
| Case-sensitive | `score` ≠ `Score` |
| No spaces | use `piece_x` not `piece x` |
| Avoid Python **keywords** | `if`, `while`, `class` illegal as names |

## Naming Styles

| Style | Example | Common for |
|-------|---------|------------|
| snake_case | `lines_cleared` | variables, functions |
| UPPER_SNAKE | `BOARD_WIDTH` | constants |
| PascalCase | `Tetromino` | class names (later) |

## Assignment Statement

```python
x = 10
```

Steps:

1. Evaluate right side (`10`)
2. Store in name `x`

### Chained assignment (rare)

```python
a = b = 0  # both zero
```

### Multiple names

```python
x, y = 4, 0  # x=4, y=0
```

Useful for positions: `piece_x, piece_y = 4, 0`

## Updating Variables

```python
score = 0
score = score + 100
```

Shorthand operators:

```python
score += 100    # score = score + 100
piece_x -= 1    # piece_x = piece_x - 1
lines *= 2
```

Tetris: `piece_x += 1` moves piece right.

## Swapping Values

```python
a = 1
b = 2
a, b = b, a
# now a=2, b=1
```

## Try It Yourself

Simulate two moves right:

```python
piece_x = 4
piece_y = 0
piece_x += 1
piece_x += 1
print(f"Position: ({piece_x}, {piece_y})")
```

## Summary

- Use **snake_case** for variables; **UPPER** for constants.
- **Assignment** `=` stores a value.
- **`+=`, `-=`** update based on old value.
- Tetris movement is updating `piece_x` / `piece_y`.

**Next:** [Updating and Displaying Values](03-updating-and-displaying.html)
