# Chapter 13: Naming and Assignment

Good names and clear assignment make code you can read **months later**. Bad names make Tetris feel impossible to fix.

This chapter covers the rules Python enforces, the style habits programmers follow, and the many ways to put a value into a variable — including shortcuts you will use every time the player moves a piece.

## Naming Rules (Python)

| Rule | Example |
|------|---------|
| Letters, numbers, underscore | `piece_x2` OK |
| Cannot **start** with digit | `2piece` illegal |
| Case-sensitive | `score` ≠ `Score` |
| No spaces | use `piece_x` not `piece x` |
| Avoid Python **keywords** | `if`, `while`, `class` illegal as names |

Keywords are reserved words Python already uses for structure. If you try `if = 5`, you get a **SyntaxError** immediately — the parser knows `if` starts a decision block, not a storage bin.

### Valid vs invalid names

```python
piece_x = 4      # valid
_piece_y = 0     # valid — leading underscore is OK
piece2 = "T"     # valid — digit after letters is OK

# 2piece = 4     # SyntaxError — starts with digit
# piece x = 4    # SyntaxError — space splits the name
```

## Naming Styles

| Style | Example | Common for |
|-------|---------|------------|
| snake_case | `lines_cleared` | variables, functions |
| UPPER_SNAKE | `BOARD_WIDTH` | constants |
| PascalCase | `Tetromino` | class names (later) |

Pick one style per category and stay consistent. A file mixing `pieceX`, `piece_x`, and `PieceX` for the same idea forces readers to wonder whether those are different things.

## Assignment Statement

```python
x = 10
```

Steps:

1. Evaluate right side (`10`)
2. Store in name `x`

Nothing prints automatically. Assignment is silent storage — you need `print(x)` to see the value.

```python
x = 10
print(x)  # expected output: 10
```

### Chained assignment (rare)

```python
a = b = 0  # both zero
print(a, b)  # expected output: 0 0
```

Both names point to the same starting value. Useful for resetting multiple counters at once: `score = lines = 0`.

### Multiple names — tuple unpacking

```python
x, y = 4, 0  # x=4, y=0
print(x, y)  # expected output: 4 0
```

Useful for positions: `piece_x, piece_y = 4, 0` spawns a piece at column 4, row 0 in one readable line.

The count on the left must match the count on the right:

```python
# a, b = 1, 2, 3  # ValueError — too many values
```

## Updating Variables

```python
score = 0
score = score + 100
print(score)  # expected output: 100
```

Python reads the old value on the right, computes the new value, then stores it back under the same name.

Shorthand operators:

```python
score += 100    # score = score + 100
piece_x -= 1    # piece_x = piece_x - 1
lines *= 2      # lines = lines * 2
piece_y //= 2   # integer division update (rare in Tetris)
```

Tetris: `piece_x += 1` moves piece right; `piece_y += 1` moves piece down one row.

### Walkthrough — three line clears

```python
score = 0
lines_cleared = 0

lines_cleared += 1
score += 100
print(score, lines_cleared)  # expected output: 100 1

lines_cleared += 1
score += 100
print(score, lines_cleared)  # expected output: 200 2
```

Each `+=` builds on the previous total — that is how scoring accumulates across a match.

## Swapping Values

```python
a = 1
b = 2
a, b = b, a
print(a, b)  # expected output: 2 1
```

Python evaluates the right side first (`b, a` becomes `2, 1`), then assigns to the left. No temporary variable needed.

In Tetris you might swap two row buffers when collapsing lines — same idea, bigger data later.

## Reassigning vs Mutating (Preview)

For simple numbers and strings, assignment **replaces** the value:

```python
piece_x = 4
piece_x = 5   # 4 is discarded; piece_x is now 5
```

Lists behave differently (Part 7) — you can change contents without changing the name. For now, treat every `=` as “put this new value in the box.”

## Common Mistakes

**Using `=` when you mean compare**

```python
# if piece_x = 4:   # SyntaxError — assignment inside if
if piece_x == 4:    # correct — comparison
    print("At spawn column")
```

**Typos in names**

```python
piece_x = 4
# piece_x += 1   # if you typo piece_xx, Python creates a NEW variable
```

Python will not warn you — `piece_xx` silently starts at zero-ish behavior. Run your code often to catch this.

**Forgetting that assignment does not copy “formulas”**

```python
offset = piece_x + 2
piece_x = 5
print(offset)  # still 6 — offset was computed once at assignment time
```

`offset` does not auto-update when `piece_x` changes unless you assign again.

## Try It Yourself

Simulate two moves right:

```python
piece_x = 4
piece_y = 0
piece_x += 1
piece_x += 1
print(f"Position: ({piece_x}, {piece_y})")
# expected output: Position: (6, 0)
```

Bonus: start at `(4, 0)`, move right once, down twice, left once. Print after each step so you see the trail of assignments.

## Summary

- Use **snake_case** for variables; **UPPER** for constants.
- **Assignment** `=` stores a value; it does not compare.
- **`+=`, `-=`** update based on old value — the core of movement and scoring.
- Tuple unpacking sets multiple variables in one line — handy for spawn positions.
- Tetris movement is updating `piece_x` / `piece_y`.

**Next:** [Updating and Displaying Values](03-updating-and-displaying.md)
