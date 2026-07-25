---
title: Numbers and Math
order: 2
---

# Chapter 9: Numbers and Math

Tetris uses numbers everywhere: **positions**, **scores**, **counts of cleared lines**. Python treats numbers as simple values you can calculate with.

## Two Main Number Types

| Type | Examples | Use |
|------|----------|-----|
| **int** | `0`, `42`, `-3` | Whole numbers — grid cells, score |
| **float** | `3.14`, `-0.5` | Decimals — less common in our Tetris |

```python
print(type(10))    # <class 'int'>
print(type(2.5))   # <class 'float'>
```

## Arithmetic Operators

```python
print(10 + 3)   # 13  addition
print(10 - 3)   # 7   subtraction
print(10 * 3)   # 30  multiplication
print(10 / 3)   # 3.333...  division (float)
print(10 // 3)  # 3   floor division (whole number)
print(10 % 3)   # 1   remainder (modulo)
print(2 ** 3)   # 8   power (2×2×2)
```

### Modulo `%` in Tetris

Useful for “every N steps” patterns:

```python
print(7 % 10)  # 7 — column within width 10
```

## Order of Operations

Python follows school math: parentheses first, then `*`, `/`, then `+`, `-`.

```python
print(2 + 3 * 4)    # 14 not 20
print((2 + 3) * 4)  # 20
```

## Assigning Numbers to Variables (Preview)

```python
score = 0
score = score + 100
print(score)  # 100
```

Shorthand:

```python
score += 100  # same as score = score + 100
```

## Converting Between Types

```python
x = int("42")      # string to int
y = float("3.14")
s = str(100)       # number to string for print
```

Invalid conversion crashes:

```python
int("hello")  # ValueError
```

## Tetris Numbers

| Concept | Variable example |
|---------|------------------|
| Piece column | `piece_x` from 0 to 9 |
| Piece row | `piece_y` from 0 to 19 |
| Board width | `WIDTH = 10` |
| Board height | `HEIGHT = 20` |
| Score | `score += 100 * lines_cleared` |

Constants in **ALL_CAPS** is a convention for values that rarely change.

## Try It Yourself

1. Compute how many points for clearing 3 lines if each line is 100 points.
2. If board width is 10, what is `9 % 10`? (last column index)
3. Print `type` of `7`, `7.0`, and `7 + 0.1`.

## Summary

- **int** = whole numbers; **float** = decimals.
- Operators: `+ - * / // % **`
- **`+=`** updates a variable.
- Tetris positions and scores are numbers.

**Next:** [Text and Strings](03-text-strings.html)
