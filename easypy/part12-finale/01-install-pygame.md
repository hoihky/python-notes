---
title: Installing Pygame
order: 1
---

# Chapter 39: Installing Pygame

**Pygame** draws windows, rectangles, and reads keyboard — without building a GUI from scratch.

## Activate Your venv

```bash
cd my_tetris
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\Activate.ps1  # Windows
```

## Install

```bash
pip install pygame
```

Add to `requirements.txt`:

```
pygame>=2.5.0
```

## Verify

```python
import pygame
print(pygame.version.ver)
```

## Minimal Window

Create `pygame_test.py`:

```python
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 40))
    pygame.display.flip()

pygame.quit()
sys.exit()
```

Run it — close window with X button.

## Pygame Event Loop

| Event | Meaning |
|-------|---------|
| `QUIT` | Window closed |
| `KEYDOWN` | Key pressed |
| `KEYUP` | Key released |

Different from text `input()` — events arrive each frame.

## Colors

```python
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
GRID_COLOR = (50, 50, 60)
```

RGB tuples 0–255.

## Coordinate System

Top-left is `(0, 0)`. `x` increases right, `y` increases **down** — same as our board rows!

## Try It Yourself

Change window size and background color. Draw one white rectangle with `pygame.draw.rect`.

## Summary

- **`pip install pygame`** in venv.
- **Event loop** + `display.flip()` refreshes screen.
- Next: **visual Tetris**.

**Next:** [Color Tetris with Graphics](02-visual-tetris.html)
