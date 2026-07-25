---
title: Color Tetris with Graphics
order: 2
---

# Chapter 40: Color Tetris with Graphics

Reuse your **Game** logic — only **drawing** and **input** change for Pygame.

## Constants for Drawing

```python
CELL = 30
WIDTH = 10
HEIGHT = 20
SCREEN_W = CELL * WIDTH + 200
SCREEN_H = CELL * HEIGHT

COLORS = {
    ".": (40, 40, 50),
    "#": (200, 200, 220),
    "I": (0, 240, 240),
    "O": (240, 240, 0),
    "T": (160, 0, 240),
    # ... more piece colors
}
```

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

## Main Loop with Keys

```python
def run_gui():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    game = Game()
    fall_timer = 0
    FALL_SPEED = 500  # ms

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

Map arrow keys to same `handle` as text version.

## Reuse Logic

**Do not rewrite** collision or line clear — import from `game.py`.

## Polish Ideas

- Show score font with `pygame.font`
- Ghost piece preview
- Next piece sidebar
- Sound effects (`pygame.mixer`)

## Try It Yourself

Add score text on screen. Change `FALL_SPEED` as lines increase.

## Summary

- **Same Game class** — new draw/input layer.
- **Clock** controls gravity timing.
- **KEYDOWN** replaces `input()`.
- You built **graphical Tetris**!

**Next:** [Congratulations and Next Steps](03-next-steps.html)
