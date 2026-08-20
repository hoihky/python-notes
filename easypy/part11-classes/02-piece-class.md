# Chapter 37: A Piece Class for Tetris

Wrap piece data and behavior in a **`Piece`** class.

Your dictionary-based game stored piece facts as separate keys. The `Piece` class bundles name, rotation, row, and column into one object — plus methods that know how to move and report occupied cells.

## piece.py

```python
from shapes import SHAPES, PIECE_LETTERS
import random
from constants import WIDTH

class Piece:
    def __init__(self, name=None, rotation=0, row=0, col=None):
        self.name = name or random.choice(PIECE_LETTERS)
        self.rotation = rotation
        self.row = row
        self.col = col if col is not None else WIDTH // 2 - 2

    def cells(self):
        offsets = SHAPES[self.name][self.rotation]
        return [(self.row + dr, self.col + dc) for dr, dc in offsets]

    def move(self, d_row, d_col):
        self.row += d_row
        self.col += d_col

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    @classmethod
    def random_spawn(cls):
        return cls()
```

### Reading the methods

- **`cells()`** — absolute board coordinates for this piece right now. Same job as `get_cells(...)` but reads from `self`.
- **`move(d_row, d_col)`** — changes position. Does not check collision — callers validate first or undo after.
- **`rotate()`** — bumps rotation with wraparound at 4.
- **`random_spawn()`** — factory for a new random piece at default spawn column.

`@classmethod` creates pieces via `Piece.random_spawn()` without needing an existing instance. `cls()` means "call `Piece` with default spawn settings."

Default column `WIDTH // 2 - 2` centers most shapes — same math you used in Part 10.

## Using Piece in can_place

Bridge from object to your existing collision function:

```python
def can_place_piece(board, piece):
    return can_place(board, piece.cells())
```

The board logic stays unchanged. Only the **source** of cell coordinates changed — from dict keys to `piece.cells()`.

```python
piece = Piece("T", rotation=0, row=5, col=4)
board = make_board()
print(can_place_piece(board, piece))  # True on empty board
```

## try_move with Piece

The **undo** pattern: try the move, revert if illegal.

```python
def try_move_piece(board, piece, d_row, d_col):
    piece.move(d_row, d_col)
    if not can_place_piece(board, piece):
        piece.move(-d_row, -d_col)  # undo
        return False
    return True
```

Why move first instead of computing `new_row`? Fewer parameters passed around — the piece already knows its position. Undo restores the previous state if `can_place` fails.

Rotation undo is slightly different because rotation wraps:

```python
def try_rotate_piece(board, piece):
    old_rot = piece.rotation
    piece.rotate()
    if not can_place_piece(board, piece):
        piece.rotation = old_rot
        return False
    return True
```

Saving `old_rot` avoids `% 4` arithmetic when reverting.

## Compare dict style vs class style

| Task | Dictionary | Piece class |
|------|------------|-------------|
| Get cells | `get_cells(state["piece_row"], ...)` | `piece.cells()` |
| Move right | `try_move(state, 0, 1)` | `try_move_piece(board, piece, 0, 1)` |
| Spawn | set four keys | `Piece.random_spawn()` |

Behavior is identical — the class version reads like a sentence about the piece.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Typo `-dc` instead of `-d_col` | NameError on undo | Match parameter names exactly |
| Checking collision inside `move()` | Hard to undo cleanly | Keep `move()` dumb; validate outside |
| Forgetting to undo rotate | Piece stuck in wall | Restore `old_rot` on failure |
| Calling `cells()` before setting name | KeyError in SHAPES | Set `name` in `__init__` first |

## Try It Yourself

Create `piece = Piece.random_spawn()`, print `piece.cells()`, call `piece.rotate()`, print again:

```python
piece = Piece.random_spawn()
print(f"{piece.name} rot {piece.rotation}:", piece.cells())
piece.rotate()
print(f"after rotate:", piece.cells())
# expected: same center, different cell offsets
```

Move the piece toward a wall on a test board and confirm `try_move_piece` returns `False` without leaving the piece outside bounds.

## Summary

- **`Piece`** holds name, rotation, position.
- **Methods** `cells()`, `move()`, `rotate()` encapsulate piece behavior.
- Invalid moves **undo** temporary position or rotation changes.
- **`can_place_piece`** connects the class to existing board logic.
- Next: **`Game` class** refactor.

**Next:** [Refactoring Tetris with Classes](03-refactoring-tetris.md)
