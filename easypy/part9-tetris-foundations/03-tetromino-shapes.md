# Chapter 29: Tetromino Shapes

Each **tetromino** is four blocks. We store **offsets** from an anchor cell `(piece_row, piece_col)`.

Instead of storing absolute board coordinates that change every frame, store **relative** steps: "one row down, zero columns over." Add the anchor when you need real positions. Move the anchor — the whole shape follows.

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

**O-piece** repeats the same offsets four times — square looks identical every rotation. **I-piece** flips between horizontal and vertical lists. **T-piece** shows four distinct rotation patterns.

Structure recap:

```
SHAPES["T"][2]  →  third rotation of T
                  → list of four (dr, dc) tuples
```

## Reading a Shape on Paper

For `T` rotation 0 at anchor `(0, 3)`:

```
offsets: (0,1), (1,0), (1,1), (1,2)
         anchor at (0,3) means (0,1) is row 0, col 3+1=4
```

Sketch the well, mark anchor, add each offset — verify four `#` form a T.

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

`random.choice` picks uniformly from the list — fair mix over many games.

List comprehension in `get_cells` builds the coordinate list in one expression — same loop logic as `get_piece_cells` from Part 8, Tetris-specific names here.

## Spawn Position

Start near top center:

```python
from constants import WIDTH

def spawn_piece():
    name, rot = random_piece()
    piece_col = WIDTH // 2 - 2
    piece_row = 0
    return name, rot, piece_row, piece_col
```

`WIDTH // 2 - 2` is a rough horizontal center for wide pieces — tweak per shape later. I-piece may need `piece_col = 3` so it does not clip the left wall.

Spawn walkthrough:

1. Pick random letter and rotation 0.
2. Place anchor row 0, column near middle.
3. Return all four values main loop stores in state.

## Test Drawing

```python
from board import make_board, draw_board
from shapes import get_cells, spawn_piece

b = make_board()
name, rot, pr, pc = "T", 0, 0, 3
cells = get_cells(pr, pc, name, rot)
draw_board(b, cells)

# try all four T rotations
for rot in range(4):
    cells = get_cells(0, 3, "T", rot)
    draw_board(b, cells)
```

Each rotation should look different except O. Board stays empty between draws — overlay only.

## Adding L-Piece (Example)

L has four rotations — three blocks vertical plus one foot:

```python
"L": [
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 0), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (2, 0), (2, 1)],
],
```

Draw each rotation at the same anchor to compare silhouettes.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Wrong rotation index | Shape jumps oddly | Keep `rotation` 0–3, wrap with `% 4` |
| Offsets mix row/col order | Broken shape | Tuple is `(dr, dc)` — row first |
| Only three blocks in list | Not a tetromino | Exactly four offsets per rotation |
| Spawn too far right | IndexError or clip | Test `get_cells` with `is_cell_free` |

## Try It Yourself

Add **L** shape with 4 rotations (3 blocks vertical + 1 on side). Draw each rotation.

**Bonus:** Write `def next_rotation(name, rotation):` returning `(name, (rotation + 1) % 4)` for press-`w` logic later.

## Summary

- Shapes = **offset lists** per rotation.
- **`random.choice`** picks next piece.
- **`get_cells`** converts anchor + shape → board coordinates.
- Spawn near top center; tune column per shape.
- Next: polish **drawing** in main loop.

**Next:** [Drawing the Grid in the Terminal](04-drawing-the-grid.md)
