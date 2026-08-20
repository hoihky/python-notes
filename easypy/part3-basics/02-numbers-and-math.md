# Chapter 9: Numbers and Math

Tetris uses numbers everywhere: **positions**, **scores**, **counts of cleared lines**. Python treats numbers as simple values you can calculate with.

The grid is really a set of numbered addresses. Row 0 is near the top; column 0 is on the left. Score starts at 0 and climbs. Every move and line clear is arithmetic in disguise.

## Two Main Number Types

| Type | Examples | Use |
|------|----------|-----|
| **int** | `0`, `42`, `-3` | Whole numbers — grid cells, score |
| **float** | `3.14`, `-0.5` | Decimals — less common in our Tetris |

```python
print(type(10))    # expected output: <class 'int'>
print(type(2.5))   # expected output: <class 'float'>
```

`type()` tells you what Python thinks a value is. Grid coordinates and scores stay **int** in text Tetris — no half a cell.

## Arithmetic Operators

```python
print(10 + 3)   # expected output: 13  (addition)
print(10 - 3)   # expected output: 7   (subtraction)
print(10 * 3)   # expected output: 30  (multiplication)
print(10 / 3)   # expected output: 3.3333333333333335  (division → float)
print(10 // 3)  # expected output: 3   (floor division → whole number)
print(10 % 3)   # expected output: 1   (remainder)
print(2 ** 3)   # expected output: 8   (power: 2×2×2)
```

Notice `/` gives a decimal even when the answer is "almost whole." Use `//` when you need an integer result — e.g. how many full rows fit in a count.

### Modulo `%` in Tetris

Useful for "every N steps" patterns:

```python
print(7 % 10)  # expected output: 7 — column within width 10
print(10 % 10) # expected output: 0 — wraps to column 0
```

If you imagine columns numbered 0–9 on a 10-wide board, `% 10` keeps a growing column counter inside that range — handy for animation or wrapping math later.

## Order of Operations

Python follows school math: parentheses first, then `*`, `/`, `//`, `%`, then `+`, `-`.

```python
print(2 + 3 * 4)    # expected output: 14 not 20
print((2 + 3) * 4)  # expected output: 20
```

When in doubt, add parentheses. Tetris score formulas like `100 * lines * level` benefit from explicit grouping so you and Python agree on order.

## Assigning Numbers to Variables (Preview)

```python
score = 0
score = score + 100
print(score)  # expected output: 100
```

Shorthand:

```python
score = 0
score += 100  # same as score = score + 100
print(score)  # expected output: 100
```

`+=` appears constantly in games: `score += 10`, `lines_cleared += 1`, `piece_y += 1` (move down one row). Same pattern, different meaning.

### Tetris-style score example

```python
lines_cleared = 2
points_per_line = 100
score = 0
score += points_per_line * lines_cleared
print(score)
# expected output: 200
```

Variables hold values that change; numbers in formulas stay plain until assigned to a name (variables get a full chapter soon).

## Converting Between Types

```python
x = int("42")      # string to int
y = float("3.14")
s = str(100)       # number to string for print
print(x, y, s)
# expected output: 42 3.14 100
```

Invalid conversion crashes:

```python
int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'
```

You will convert often when reading keyboard input — everything from `input()` arrives as text even if the user typed digits.

## Tetris Numbers

| Concept | Variable example |
|---------|------------------|
| Piece column | `piece_x` from 0 to 9 |
| Piece row | `piece_y` from 0 to 19 |
| Board width | `WIDTH = 10` |
| Board height | `HEIGHT = 20` |
| Score | `score += 100 * lines_cleared` |

Constants in **ALL_CAPS** is a convention for values that rarely change.

Standard Tetris wells are 10 wide and 20 tall — **240** cell addresses total. You will not memorize that; but knowing width and height as named constants keeps magic numbers out of your code.

### Step-by-step: last column index

A 10-wide board uses columns **0 through 9**:

```python
WIDTH = 10
first_column = 0
last_column = WIDTH - 1
print(last_column)
# expected output: 9
```

If `piece_x` is ever `10`, the piece is partly off the right edge — collision code will catch that later using comparisons, not guesswork.

## Common Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Using `/` when you need whole cells | `10 / 2` is `5.0` (float) | Use `//` for integer division |
| Confusing `%` with `/` | `10 % 3` is remainder `1`, not `3.33` | `%` = leftover after division |
| `"42" + 1` | `TypeError` — string plus int | `int("42") + 1` |
| Forgetting parentheses in formulas | Wrong score | Use `(a + b) * c` when needed |

## Try It Yourself

1. Compute how many points for clearing 3 lines if each line is 100 points.
2. If board width is 10, what is `9 % 10`? (last column index)
3. Print `type` of `7`, `7.0`, and `7 + 0.1`.

Check your answers:

```python
print(3 * 100)       # expected output: 300
print(9 % 10)        # expected output: 9
print(type(7))       # expected output: <class 'int'>
print(type(7.0))     # expected output: <class 'float'>
print(type(7 + 0.1)) # expected output: <class 'float'>
```

## Summary

- **int** = whole numbers; **float** = decimals.
- Operators: `+ - * / // % **`
- **`+=`** updates a variable.
- Tetris positions and scores are numbers.

**Next:** [Text and Strings](03-text-strings.md)
