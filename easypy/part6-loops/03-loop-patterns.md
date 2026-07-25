---
title: Loop Patterns You Will Use Often
order: 3
---

# Chapter 20: Loop Patterns You Will Use Often

These patterns appear in almost every game — including Tetris. Recognizing them saves time.

## Pattern 1 — Count Up

```python
score = 0
for _ in range(4):
    score += 100
```

`_` means “I don’t need this index variable.”

## Pattern 2 — Search (Find Something)

```python
found = False
for row in range(HEIGHT):
    if row_is_full(row):
        found = True
        break
```

## Pattern 3 — Accumulate String

```python
row_string = ""
for col in range(WIDTH):
    row_string += "."
print(row_string)
```

## Pattern 4 — Enumerate with Index

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
```

Useful when row number matters.

## Pattern 5 — Game Loop + Input

```python
game_over = False
while not game_over:
    draw_board()
    cmd = input("Move: ")
    handle_command(cmd)
    update_game()
    if should_end():
        game_over = True
```

We split into functions later.

## Pattern 6 — Clear Full Lines (Sketch)

```python
for row in range(HEIGHT - 1, -1, -1):  # bottom to top
    if is_row_full(row):
        remove_row(row)
        score += 100
```

Backward loop helps when rows shift down.

## Avoid Off-by-One Errors

Board width 10 → valid columns `0` to `9`:

```python
for col in range(10):  # 0..9 OK
    pass
# col < 10 also OK in while
```

## Try It Yourself

Write nested loops printing:

```
.....
...#.
..###.
```

(hint: use `if` inside inner loop on `col` and `row`)

## Summary

- **Accumulate**, **search**, **nested grid**, **game loop** are core patterns.
- Watch **0-based** indices on a width-10 board.
- Next: **lists** — better than separate variables.

**Next:** [Lists](../part7-collections/01-lists.html)
