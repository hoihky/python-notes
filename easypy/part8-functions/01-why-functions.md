---
title: Why Functions?
order: 1
---

# Chapter 24: Why Functions?

A **function** is a named recipe — a group of lines you run whenever you call the name. Without functions, Tetris becomes one endless file of copy-paste.

## The Problem Without Functions

```python
# draw board — copy 1
for row in board:
    print("".join(row))

# ... 50 lines later ...

# draw board — copy 2 (oops, you fixed a bug in only one place)
```

## The Solution

```python
def draw_board(board):
    for row in board:
        print("".join(row))

draw_board(board)
draw_board(board)  # same behavior, one definition
```

## Benefits

| Benefit | Tetris example |
|---------|----------------|
| **Reuse** | Draw after every move |
| **Readability** | `move_piece()` says what it does |
| **Easier fixes** | Change draw logic once |
| **Team work** | One person writes `clear_lines` |

## Analogy

A function is like a **button** on a microwave:

- **Name** on button — `def heat_pizza()`
- **Instructions inside** — what happens when pressed
- **Press** — **call** the function

## Built-in Functions You Know

- `print()`
- `len()`
- `input()`
- `range()`
- `int()`, `str()`

You will define your own.

## Tetris Functions We Will Write

| Function | Job |
|----------|-----|
| `make_board()` | Empty grid |
| `draw_board()` | Show grid |
| `can_move()` | Collision check |
| `lock_piece()` | Merge piece into board |
| `clear_lines()` | Remove full rows |
| `new_piece()` | Random shape |

## Try It Yourself

Without looking ahead, list on paper 5 tasks Tetris does each turn. Each might become a function.

## Summary

- **Functions** group reusable steps.
- They make Tetris **maintainable**.
- Next: how to **define** and **call** them.

**Next:** [Defining and Calling Functions](02-defining-functions.html)
