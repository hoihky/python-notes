---
title: Tetromino Shapes
order: 3
---

# Chapter 29: Tetromino Shapes

Each **tetromino** is four blocks. We store **offsets** from an anchor cell `(piece_row, piece_col)`.

## shapes.py

```python
# Each shape: list of rotations; each rotation: list of (dr, dc)

SHAPES = {
    "O": [
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)],
    ],
    "I": [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
    ],
    "T": [
        [(0, 1), (1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 1), (1, 2), (2, 1)],
        [(1, 0), (1, 1), (1, 2), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 1)],
    ],
    # Add S, Z, J, L similarly — or copy from course repo
}

PIECE_LETTERS = list(SHAPES.keys())
```

`dr` = row offset, `dc` = column offset.

## Helper Functions

```python
import random
from shapes import SHAPES, PIECE_LETTERS

def random_piece():
    name = random.choice(PIECE_LETTERS)
    return name, 0  # name and rotation index

def get_cells(piece_row, piece_col, name, rotation):
    offsets = SHAPES[name][rotation]
    return [(piece_row + dr, piece_col + dc) for dr, dc in offsets]
```

## Spawn Position

Start near top center:

```python
def spawn_piece():
    name, rot = random_piece()
    piece_col = WIDTH // 2 - 2
    piece_row = 0
    return name, rot, piece_row, piece_col
```

Adjust per shape so pieces appear centered.

## Test Drawing

```python
from board import make_board, draw_board
from shapes import get_cells  # you export helpers

b = make_board()
name, rot, pr, pc = "T", 0, 0, 3
cells = get_cells(pr, pc, name, rot)
draw_board(b, cells)
```

## Try It Yourself

Add **L** shape with 4 rotations (3 blocks vertical + 1 on side). Draw each rotation.

## Summary

- Shapes = **offset lists** per rotation.
- **`random.choice`** picks next piece.
- **`get_cells`** converts anchor + shape → board coordinates.
- Next: polish **drawing** in main loop.

**Next:** [Drawing the Grid in the Terminal](04-drawing-the-grid.html)
