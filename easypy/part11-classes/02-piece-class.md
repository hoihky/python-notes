---
title: A Piece Class for Tetris
order: 2
---

# Chapter 37: A Piece Class for Tetris

Wrap piece data and behavior in a **`Piece`** class.

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

`@classmethod` creates pieces via `Piece.random_spawn()`.

## Using Piece in can_place

```python
def can_place_piece(board, piece):
    return can_place(board, piece.cells())
```

## try_move with Piece

```python
def try_move_piece(board, piece, d_row, d_col):
    piece.move(d_row, d_col)
    if not can_place_piece(board, piece):
        piece.move(-d_row, -d_col)  # undo
        return False
    return True
```

Undo trick: move back if invalid.

## Try It Yourself

Create `piece = Piece.random_spawn()`, print `piece.cells()`, call `piece.rotate()`, print again.

## Summary

- **`Piece`** holds name, rotation, position.
- **Methods** `cells()`, `move()`, `rotate()`.
- Invalid moves **undo** temporary position change.
- Next: **`Game` class** refactor.

**Next:** [Refactoring Tetris with Classes](03-refactoring-tetris.html)
