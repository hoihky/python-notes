# Chapter 38: Refactoring Tetris with Classes

Replace the big `state` dictionary with a **`Game`** class — cleaner and closer to how professional games are structured.

**Refactoring** means changing code structure without changing what the player experiences. Your text Tetris should play the same after this chapter — but files and names should make more sense when you open the project six months later.

## Why a Game class?

The dictionary approach stored everything in one bag:

```python
state = {
    "board": ...,
    "piece_row": ...,
    "score": ...,
    "lines": ...,
    "game_over": ...,
}
```

Any function could read or write any key. A `Game` class says: **this object owns the match** — board, active piece, score, and the rules for one turn.

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

Adapt `clear_full_lines` to return count or update `Game` methods to match your Part 10 code. If your Part 10 version mutates a `state` dict instead of returning a count, wrap it:

```python
def clear_full_lines_board(board):
    # your existing logic; return number cleared
    ...
```

Then call that from `lock_and_spawn`.

## Method map: what moved where

| Old function | New home |
|--------------|----------|
| `try_move(state, ...)` | `Game.try_move` |
| `try_rotate(state)` | `Game.try_rotate` |
| `tick_gravity(state)` | `Game.tick` |
| `lock_piece(state)` | `Game.lock_and_spawn` |
| `handle_input(state, cmd)` | `Game.handle` |
| `draw_game(state)` | `Game.draw` |

The **rules** did not change — only where they live.

## Benefits

| Before (dict) | After (classes) |
|---------------|-----------------|
| `state["piece_row"]` | `game.piece.row` |
| Many loose functions | Methods on `Game` |
| Easy to lose keys | Structure enforced |
| Hard to see ownership | `Game` clearly owns the match |

IDE autocomplete on `game.` lists available actions. Typos like `state["scroe"]` become less likely when you use `game.score`.

## Refactoring safely

1. Make `Piece` work with your existing `can_place` (previous chapter).
2. Create `Game` with the same behavior as your dict loop.
3. Run the playtest checklist from Chapter 35 — everything should still pass.
4. Delete old dict-based code only after the class version runs.

Small steps beat rewriting everything in one sitting.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| `clear_full_lines` mismatch | Score never updates | Align return value with `lock_and_spawn` |
| Drawing inside `lock_and_spawn` | Mixed concerns | Keep draw in main loop only |
| Skipping spawn collision check | Overlap at game over | Call `can_place_current` after spawn |
| Two sources of truth | Dict and Game both exist | Remove old `state` once migrated |

## Optional: hard drop on Game

```python
def hard_drop(self):
    while self.try_move(1, 0):
        pass
    self.lock_and_spawn()
```

Wire to `handle` with a new key when ready.

## Try It Yourself

Refactor your working text Tetris to use `Game` and `Piece`. Run and compare behavior side by side with your Part 10 version — same score rules, same controls, same game over.

Keep a backup branch or copy of `game_logic.py` until you trust the class version.

## Summary

- **`Game`** owns board, piece, score, loop logic.
- **`Piece`** owns shape position and movement helpers.
- Classes **group** related data and behavior without changing Tetris rules.
- Refactor in small steps; verify with the same playtest checklist.
- Next: **Pygame** for graphics.

**Next:** [Installing Pygame](../part12-finale/01-install-pygame.md)
