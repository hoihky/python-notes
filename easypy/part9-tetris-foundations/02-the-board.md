# Chapter 28: Building the Board

Create **`constants.py`** and **`board.py`** — foundation of the game.

Every Tetris function will ask: "How wide? How tall? What character means empty?" Centralizing answers in `constants.py` stops magic numbers scattered through your code. `board.py` owns the grid itself — create it, draw it, ask if a cell is free.

## constants.py

```python
WIDTH = 10
HEIGHT = 20

EMPTY = "."
BLOCK = "#"
```

Why name `EMPTY` and `BLOCK`?

- Change `.` to ` ` (space) later — one edit.
- Compare with `== EMPTY` instead of guessing `"."` everywhere.
- Readers see intent: empty cell vs filled block.

Standard Tetris well is 10 wide, 20 tall. Keep these as constants even while experimenting — if you shrink height for debugging, change `HEIGHT` once.

## board.py

```python
from constants import WIDTH, HEIGHT, EMPTY, BLOCK

def make_board():
    """Return empty HEIGHT x WIDTH grid."""
    return [[EMPTY] * WIDTH for _ in range(HEIGHT)]

def draw_board(board, piece_cells=None, piece_char=BLOCK):
    """
    Draw board. piece_cells: list of (row, col) for falling piece.
    """
    display = [row[:] for row in board]  # copy
    if piece_cells:
        for r, c in piece_cells:
            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                display[r][c] = piece_char
    print("\n" * 2)
    for row in display:
        print("".join(row))

def is_cell_free(board, row, col):
    if row < 0 or row >= HEIGHT or col < 0 or col >= WIDTH:
        return False
    return board[row][col] == EMPTY
```

### Step-by-step: `make_board`

1. List comprehension runs `HEIGHT` times.
2. Each iteration builds one row of `WIDTH` copies of `EMPTY`.
3. Returns fresh 2D list — ready for play.

### Step-by-step: `draw_board`

1. **Copy** every row into `display` — do not touch locked `board`.
2. If falling piece cells exist, paint them on `display` only.
3. Bounds check `0 <= r < HEIGHT` skips cells that stick out above the well (some rotations spawn partly off-screen).
4. Print blank lines, then each row joined into a string.

### Step-by-step: `is_cell_free`

1. Outside the rectangle? Not free (treat walls as solid).
2. Inside and cell is `EMPTY`? Free.
3. Inside and cell is `BLOCK`? Not free — collision.

Returns **boolean** — perfect for `if is_cell_free(...)` chains in move logic later.

## Test It

```python
# at bottom of board.py
if __name__ == "__main__":
    b = make_board()
    draw_board(b)
    # fake piece cells — O-piece at top
    cells = [(0, 4), (0, 5), (1, 4), (1, 5)]
    draw_board(b, cells)
```

Run:

```bash
python3 board.py
```

You should see empty grid, then O-shape on top. Run twice — second draw should still show empty **board** if you only overlay on copy (the locked board never gained `#`).

Verify freedom checks:

```python
if __name__ == "__main__":
    b = make_board()
    print(is_cell_free(b, 0, 0))   # True
    b[19][5] = BLOCK
    print(is_cell_free(b, 19, 5))  # False
    print(is_cell_free(b, -1, 0))  # False — above top
```

## Why Copy for Display?

We must not permanently draw falling piece onto `board` until lock — overlay on **copy** for drawing only.

If you wrote `board[r][c] = BLOCK` every frame for the falling piece, then moved left, old `#` cells would remain — trails of blocks across the well. Copy-on-draw avoids that entirely.

## `fill_row` — Practice Helper

```python
def fill_row(board, row_index):
    """Set one entire row to blocks — useful for testing line clear."""
    board[row_index] = [BLOCK] * WIDTH

# test
if __name__ == "__main__":
    b = make_board()
    fill_row(b, HEIGHT - 1)
    draw_board(b)
    # expected: bottom row all '#'
```

## Common Mistakes

| Mistake | What you see | Fix |
|---------|--------------|-----|
| Import constants wrong | `NameError: WIDTH` | `from constants import WIDTH, ...` |
| Skip bounds check when drawing | IndexError on rotation | Keep `0 <= r < HEIGHT` guard |
| Mutate `board` in `draw_board` | Stuck piece trails | Only modify `display` copy |
| Compare to `"."` directly | Breaks if EMPTY changes | Use `== EMPTY` |

## Try It Yourself

Add a function `def fill_row(board, row_index):` setting one row to all `#`. Test drawing.

**Bonus:** Add `def count_empty_in_row(board, row_index):` returning how many `EMPTY` cells remain — groundwork for line clearing.

## Summary

- **`constants.py`** centralizes sizes and symbols.
- **`make_board`**, **`draw_board`**, **`is_cell_free`** are core.
- Falling piece drawn via **overlay** on copy.
- **`if __name__ == "__main__"`** blocks are your quick tests.
- Next: **shape definitions**.

**Next:** [Tetromino Shapes](03-tetromino-shapes.md)
