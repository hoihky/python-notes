# Chapter 20: Loop Patterns You Will Use Often

These patterns appear in almost every game — including Tetris. Recognizing them saves time.

Instead of inventing a new structure every chapter, you will reuse the same shapes: count, search, build a string, walk a grid, run until game over. Learn the pattern name once; apply it everywhere.

## Pattern 1 — Count Up

```python
score = 0
for _ in range(4):
    score += 100
print(score)
# expected output: 1000
```

`_` means “I don’t need this index variable.” Same idea as repeating `score += 100` four times without copy-paste.

With `while`:

```python
score = 0
n = 0
while n < 4:
    score += 100
    n += 1
print(score)
# expected output: 1000
```

Pick `for` when you know how many times; `while` when stopping depends on game state.

## Pattern 2 — Search (Find Something)

```python
HEIGHT = 20
found = False
for row in range(HEIGHT):
    if row_is_full(row):  # pretend function — returns True/False
        found = True
        break
print("Found full row?", found)
```

Search loops start with a default (`found = False`), scan until success, then **`break`** early. Tetris line detection: walk rows bottom-up, stop at first full row or collect all full rows.

Without `break`, you keep scanning after finding what you need — wasted work.

## Pattern 3 — Accumulate String

```python
WIDTH = 10
row_string = ""
for col in range(WIDTH):
    row_string += "."
print(row_string)
# expected output: ..........
print(len(row_string))
# expected output: 10
```

One character at a time builds a row for printing. Same pattern builds `"##....."` when you branch on `col` with `if`.

For many small joins, lists join faster (Part 7) — but the accumulate-string pattern is the clearest starting point.

## Pattern 4 — Enumerate with Index

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
```

Expected output:

```
0 a
1 b
2 c
```

Useful when row number matters — e.g. printing “Row 3: .........” without manual counter:

```python
for row_index, row_data in enumerate(["....", "#..."]):
    print(row_index, row_data)
# expected output: 0 ....
#                   1 #...
```

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

We split into functions later. The pattern is fixed: **draw → input → update → check end**. Tetris never skips draw after an update — the player must see the new state.

Pseudocode names (`draw_board`, etc.) stand in until you wire real code.

## Pattern 6 — Clear Full Lines (Sketch)

```python
HEIGHT = 20
score = 0
for row in range(HEIGHT - 1, -1, -1):  # bottom to top: 19, 18, ..., 0
    if is_row_full(row):
        remove_row(row)
        score += 100
```

Backward loop helps when rows shift down — removing row 10 before row 5 avoids skipping a row after collapse. You will implement `is_row_full` and `remove_row` when the board is a list of lists.

## Pattern 7 — Filter / Skip with continue

```python
for row in range(10):
    if row % 2 == 1:
        continue  # skip odd rows in this example
    print("Even row", row)
```

Expected output: even rows 0,2,4,6,8. In Tetris, `continue` might skip empty rows during a debug print pass.

## Pattern 8 — Nested Grid with Coordinates

```python
for row in range(4):
    for col in range(5):
        print(f"cell ({col}, {row})")
```

Visits every coordinate once — mental model for collision: “for each cell the piece would occupy, is it blocked?”

## Avoid Off-by-One Errors

Board width 10 → valid columns `0` to `9`:

```python
for col in range(10):  # 0..9 OK
    pass
# col < 10 also OK in while
```

| Intent | Correct loop |
|--------|----------------|
| All columns | `range(10)` or `range(BOARD_WIDTH)` |
| Inner playable width | still `0 .. WIDTH-1` |
| “10th column” as humans count | index `9` in code |

When a loop runs one too many times, you often see index out of range or an extra blank column — print `col` inside the loop while debugging.

## Common Mistakes

**Forgetting to reset accumulators**

```python
for row in range(3):
    line = ""  # must be INSIDE outer loop — new line each row
    for col in range(5):
        line += "."
    print(line)
```

If `line = ""` sits **above** the outer loop only once, row 2 keeps growing from row 1’s leftovers.

**Search without break when you only need first hit**

Scans entire board every time — fine for small grids, slow later.

**Using `for` for game loop when condition is unknown**

`while not game_over` reads clearer than guessing iteration count.

## Try It Yourself

Write nested loops printing:

```
.....
...#.
..###.
```

Hint: use `if` inside inner loop on `col` and `row` — e.g. set `#` when `(row, col)` matches points on a small pyramid. Print one row per outer iteration.

Expected: three lines, five characters wide — center `#` grows with row index.

## Summary

- **Accumulate**, **search**, **nested grid**, **game loop** are core patterns — reuse them.
- **`break`** stops search early; **`continue`** skips one iteration.
- **`enumerate`** gives index + value when row numbers matter.
- Watch **0-based** indices on a width-10 board — `range(10)` not `range(11)`.
- Next: **lists** — better than separate variables.

**Next:** [Lists](../part7-collections/01-lists.md)
