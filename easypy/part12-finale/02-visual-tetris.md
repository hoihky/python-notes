# Chapter 40: Color Tetris with Graphics

Reuse your **Game** logic — only **drawing** and **input** change for Pygame.

This is the payoff chapter. You are not rewriting Tetris from scratch. You are wrapping the `Game` class from Part 11 in a graphical shell — colored cells, smooth timing, arrow keys.

## Architecture: two layers

```
┌─────────────────────────────┐
│  Pygame layer               │  draw cells, read keys, clock
│  (this chapter)             │
├─────────────────────────────┤
│  Game / Piece logic         │  collision, lock, score
│  (Part 10–11)               │
└─────────────────────────────┘
```

Keep logic imports separate from `pygame` imports where possible — it makes testing easier and mirrors how larger games split engine from rules.

## Constants for Drawing

```python
CELL = 30
WIDTH = 10
HEIGHT = 20
SCREEN_W = CELL * WIDTH + 200   # extra space for score sidebar
SCREEN_H = CELL * HEIGHT

COLORS = {
    ".": (40, 40, 50),
    "#": (200, 200, 220),
    "I": (0, 240, 240),
    "O": (240, 240, 0),
    "T": (160, 0, 240),
    "S": (0, 240, 0),
    "Z": (240, 0, 0),
    "J": (0, 0, 240),
    "L": (240, 160, 0),
}
```

`CELL = 30` means each board square is 30×30 pixels. The extra 200 pixels on `SCREEN_W` leaves room for score text or a next-piece preview later.

Map locked blocks and active piece letters to colors so each shape is easy to spot.

## Draw Grid

```python
import pygame

def draw_cell(screen, row, col, color):
    x = col * CELL
    y = row * CELL
    pygame.draw.rect(screen, color, (x, y, CELL - 1, CELL - 1))

def draw_board_gui(screen, board, piece):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            color = COLORS.get(cell, COLORS["#"])
            draw_cell(screen, r, c, color)
    for r, c in piece.cells():
        if r >= 0:
            draw_cell(screen, r, c, COLORS.get(piece.name, (255, 255, 255)))
```

Draw order matters:

1. Paint locked board cells first.
2. Paint active piece on top so it is always visible.

`CELL - 1` leaves a one-pixel gap so cells look like a grid instead of one solid blob.

### Optional: background and sidebar

```python
screen.fill((20, 20, 30))
draw_board_gui(screen, game.board, game.piece)
# score text at x = WIDTH * CELL + 20
```

## Main Loop with Keys

```python
def run_gui():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Easy Python Tetris")
    clock = pygame.time.Clock()
    game = Game()
    fall_timer = 0
    FALL_SPEED = 500  # ms between gravity ticks

    running = True
    while running:
        dt = clock.tick(60)
        fall_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.handle("a")
                elif event.key == pygame.K_RIGHT:
                    game.handle("d")
                elif event.key == pygame.K_DOWN:
                    game.handle("s")
                elif event.key == pygame.K_UP:
                    game.handle("w")
                elif event.key == pygame.K_q:
                    running = False

        if fall_timer >= FALL_SPEED:
            game.tick()
            fall_timer = 0

        screen.fill((20, 20, 30))
        draw_board_gui(screen, game.board, game.piece)
        pygame.display.flip()

        if game.game_over:
            running = False

    pygame.quit()
```

Map arrow keys to same `handle` letters as text version — your `Game.handle` does not need to know about Pygame key constants.

### Timing explained

- **`clock.tick(60)`** — cap at ~60 frames per second; returns milliseconds since last frame.
- **`fall_timer`** — accumulates time until `FALL_SPEED` ms pass, then calls `game.tick()` once.

Text Tetris fell one row per key press. Graphical Tetris falls on a **timer** while still accepting instant key responses — much closer to the arcade feel.

## Reuse Logic

**Do not rewrite** collision or line clear — import from `game.py`:

```python
from game import Game
```

If `clear_full_lines` lives elsewhere, import it there too. One source of truth prevents "text Tetris and GUI Tetris behave differently" bugs.

## Showing score with pygame.font

```python
font = pygame.font.SysFont(None, 28)

def draw_hud(screen, game):
    text = font.render(f"Score: {game.score}", True, (220, 220, 220))
    screen.blit(text, (WIDTH * CELL + 20, 20))
    lines_text = font.render(f"Lines: {game.lines}", True, (220, 220, 220))
    screen.blit(lines_text, (WIDTH * CELL + 20, 50))
```

Call `draw_hud` after the board each frame.

## Polish Ideas

- Show score font with `pygame.font`
- Ghost piece preview (draw semi-transparent cells where piece would land)
- Next piece sidebar
- Sound effects (`pygame.mixer`)
- Speed up `FALL_SPEED` as `game.lines` increases

Each polish item is optional — ship a working colored grid first, then add one enhancement at a time.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Calling `input()` in GUI loop | Window freezes | Use `KEYDOWN` events only |
| No `clock.tick` | Game runs too fast | Limit FPS and use timer for gravity |
| Wrong y/x order in `draw_cell` | Grid mirrored or shifted | `x = col`, `y = row` |
| Rewriting Game in pygame file | Two diverging codebases | Import `Game`, don't duplicate |
| Forgetting `pygame.quit()` | Hang on exit | Quit after loop ends |

## Try It Yourself

Add score text on screen. Change `FALL_SPEED` as lines increase:

```python
FALL_SPEED = max(100, 500 - game.lines * 20)
```

Lower ms = faster fall. Cap with `max` so the game stays playable.

Add `K_SPACE` for hard drop if you implemented `Game.hard_drop`.

## Summary

- **Same Game class** — new draw/input layer only.
- **Clock** controls gravity timing independent of frame rate.
- **KEYDOWN** replaces `input()`; loop runs continuously.
- Draw board then piece; flip once per frame.
- You built **graphical Tetris**!

**Next:** [Congratulations and Next Steps](03-next-steps.md)
