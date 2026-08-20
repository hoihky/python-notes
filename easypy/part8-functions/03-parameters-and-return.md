# Chapter 26: Parameters and Return Values

Functions become powerful when they **take** board state and **return** updated state or True/False answers.

Think of each function as a small machine: data goes in through parameters, something happens inside, and results leave through `return`. Tetris needs many yes/no questions ("can this piece move left?") and many transformed lists ("which cells does this shape occupy?").

## Returning Booleans

```python
def is_inside_board(col, row, width, height):
    if col < 0 or col >= width:
        return False
    if row < 0 or row >= height:
        return False
    return True

print(is_inside_board(9, 0, 10, 20))   # True
print(is_inside_board(10, 0, 10, 20))  # False
print(is_inside_board(-1, 5, 10, 20))  # False
```

Each `return False` **exits immediately** — no need to keep checking. The final `return True` means all tests passed.

Use booleans in `if`:

```python
if is_inside_board(3, 18, 10, 20):
    print("Cell is on the board")
```

## Returning New Data vs Mutating

Lists can change **in place**:

```python
def fill_bottom_row(board):
    board[-1] = ["#"] * len(board[0])

b = [["."] * 5 for _ in range(3)]
fill_bottom_row(b)
print(b[-1])  # ['#', '#', '#', '#', '#']
```

The function did not return anything, but the **same** board list changed. Callers must know whether a function mutates shared data or builds fresh data.

Or return new board (less common for us):

```python
def copy_board(board):
    return [row[:] for row in board]

original = [["."] * 3]
snapshot = copy_board(original)
snapshot[0][0] = "#"
print(original[0][0])  # .
print(snapshot[0][0])  # #
```

**Mutate** when updating the live game board. **Copy** when you need a snapshot for drawing overlays without touching locked blocks.

## Default Parameters

```python
def make_row(width=10, char="."):
    return [char] * width

print(make_row())           # 10 dots
print(make_row(5))          # 5 dots
print(make_row(5, "#"))     # ['#', '#', '#', '#', '#']
```

Defaults let callers skip arguments they usually do not care about. `make_row()` alone is enough for a standard Tetris row.

Defaults must come after non-default parameters:

```python
# def bad(a=1, b):  # SyntaxError
def good(b, a=1):
    return b + a
```

## Early return

```python
def can_place(board, cells):
    for row, col in cells:
        if row < 0 or row >= len(board):
            return False
        if col < 0 or col >= len(board[0]):
            return False
        if board[row][col] != ".":
            return False
    return True
```

Stop as soon as you know the answer. If one cell is blocked, there is no reason to check the rest — return `False` immediately.

## Tetris — Cells from Piece

Piece at anchor `(piece_row, piece_col)` with offsets:

```python
def get_piece_cells(piece_row, piece_col, shape_offsets):
    cells = []
    for dr, dc in shape_offsets:
        r = piece_row + dr
        c = piece_col + dc
        cells.append((r, c))
    return cells

offsets = [(0, 0), (0, 1), (1, 0), (1, 1)]  # O-piece
cells = get_piece_cells(0, 4, offsets)
print(cells)
# expected: [(0, 4), (0, 5), (1, 4), (1, 5)]
```

Walkthrough:

1. Start with empty list `cells`.
2. For each offset, add anchor row/col to get board coordinates.
3. Return the full list — four tuples for a tetromino.

## Combining Helpers

```python
def try_move(board, cells, drow, dcol):
    moved = [(r + drow, c + dcol) for r, c in cells]
    if can_place(board, moved):
        return moved
    return cells  # stay put if illegal

board = [["."] * 6 for _ in range(4)]
start = get_piece_cells(0, 1, [(0, 0), (0, 1)])
after = try_move(board, start, 0, 1)
print(after)  # [(0, 2), (0, 3)] — moved right
```

Small functions chain together. The game loop stays short; each helper does one job.

## Main Program Structure

```python
def main():
    board = make_board()
    draw_board(board)

if __name__ == "__main__":
    main()
```

Running the file calls `main()` — standard Python pattern.

Why the guard?

- **Import safety:** Other files can `import board` without auto-running the game.
- **Clarity:** "Start here" is obvious.

When you run `python3 board.py`, Python sets `__name__` to `"__main__"` and `main()` runs. When imported, `__name__` is the module name and the block is skipped.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgetting `return` in a helper | Caller gets `None` | Add `return` with the value |
| Default arg before required arg | SyntaxError | Required params first |
| Assuming function copied the board | Locked blocks change unexpectedly | Document mutate vs copy |
| Checking collision after moving | Piece overlaps walls | Build `moved` cells, then `can_place` |

## Try It Yourself

Write `def count_filled(row):` returning how many `#` in a row list.

```python
row = [".", "#", "#", ".", "#"]
print(count_filled(row))  # expected: 3
```

**Bonus:** Write `def is_row_full(row, empty="."):` returning `True` when no empty cells remain — line-clear preview.

## Summary

- Functions **return** results: numbers, lists, booleans.
- **Default parameters** optional arguments.
- **Early return** keeps collision code simple.
- **`if __name__ == "__main__"`** entry point.
- Ready for **Tetris Part 9**.

**Next:** [How Tetris Works](../part9-tetris-foundations/01-game-design-overview.md)
