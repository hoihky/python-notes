---
title: Refactoring Tetris with Classes
order: 3
---

# Chapter 38: Refactoring Tetris with Classes

Replace the big `state` dictionary with a **`Game`** class — cleaner and closer to how professional games are structured.

## game.py (Sketch)

```python
from board import make_board, draw_board, lock_cells, clear_full_lines
from piece import Piece
from constants import BLOCK

class Game:
    def __init__(self):
        self.board = make_board()
        self.piece = Piece.random_spawn()
        self.score = 0
        self.lines = 0
        self.game_over = False
        if not self.can_place_current():
            self.game_over = True

    def can_place_current(self):
        from collision import can_place
        return can_place(self.board, self.piece.cells())

    def draw(self):
        draw_board(self.board, self.piece.cells(), self.score, self.lines)

    def handle(self, cmd):
        if cmd == "q":
            self.game_over = True
        elif cmd == "a":
            self.try_move(0, -1)
        elif cmd == "d":
            self.try_move(0, 1)
        elif cmd == "w":
            self.try_rotate()
        elif cmd == "s":
            self.try_move(1, 0)

    def try_move(self, dr, dc):
        self.piece.move(dr, dc)
        if not self.can_place_current():
            self.piece.move(-dr, -dc)
            return False
        return True

    def try_rotate(self):
        self.piece.rotate()
        if not self.can_place_current():
            self.piece.rotation = (self.piece.rotation - 1) % 4

    def tick(self):
        if not self.try_move(1, 0):
            self.lock_and_spawn()

    def lock_and_spawn(self):
        for r, c in self.piece.cells():
            if r >= 0:
                self.board[r][c] = BLOCK
        cleared = clear_full_lines(self.board)
        if cleared:
            self.lines += cleared
            self.score += cleared * 100
        self.piece = Piece.random_spawn()
        if not self.can_place_current():
            self.game_over = True

def main():
    game = Game()
    while not game.game_over:
        game.draw()
        cmd = input("> ").strip().lower()
        game.handle(cmd)
        game.tick()
    game.draw()
    print("Game Over!", game.score)

if __name__ == "__main__":
    main()
```

Adapt `clear_full_lines` to return count or update `Game` methods to match your Part 10 code.

## Benefits

| Before (dict) | After (classes) |
|---------------|-----------------|
| `state["piece_row"]` | `game.piece.row` |
| Many loose functions | Methods on `Game` |
| Easy to lose keys | Structure enforced |

## Try It Yourself

Refactor your working text Tetris to use `Game` and `Piece`. Run and compare behavior.

## Summary

- **`Game`** owns board, piece, score, loop logic.
- **`Piece`** owns shape position.
- Classes **group** related data and behavior.
- Next: **Pygame** for graphics.

**Next:** [Installing Pygame](../part12-finale/01-install-pygame.html)
