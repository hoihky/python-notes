# Chapter 39: Installing Pygame

**Pygame** draws windows, rectangles, and reads keyboard — without building a GUI from scratch.

Until now, your game lived in the terminal. Pygame opens a window, paints colored squares for each cell, and listens for keys every frame. The **rules** stay in your `Game` class — Pygame only handles eyes and fingers.

## Activate Your venv

Always install packages inside the same virtual environment you use to run Tetris:

```bash
cd my_tetris
source venv/bin/activate   # Mac/Linux
# .\venv\Scripts\Activate.ps1  # Windows
```

Your shell prompt often shows `(venv)` when active. If you skip this step, `pip` might install Pygame for the wrong Python.

## Install

```bash
pip install pygame
```

Pin the version in `requirements.txt` so you (or a friend) can recreate the setup later:

```
pygame>=2.5.0
```

Install from the file:

```bash
pip install -r requirements.txt
```

## Verify

Quick sanity check in the REPL or a one-line script:

```python
import pygame
print(pygame.version.ver)
# expected output: something like 2.5.2 (version may vary)
```

If import fails, confirm venv is active and `pip show pygame` lists the package.

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

What each line does:

- **`pygame.init()`** — start subsystems (display, events, etc.).
- **`set_mode((400, 300))`** — create a 400×300 pixel window.
- **`event.get()`** — fetch clicks, keys, and close events since last frame.
- **`screen.fill(...)`** — paint background color (RGB).
- **`display.flip()`** — show the new frame (double buffering).
- **`pygame.quit()`** — clean shutdown.

## Pygame Event Loop

Text Tetris used blocking `input()` — the program **stopped** until the player typed. Pygame is **real-time**: the loop runs many times per second whether or not anyone presses a key.

| Event | Meaning |
|-------|---------|
| `QUIT` | Window closed (X button) |
| `KEYDOWN` | Key pressed |
| `KEYUP` | Key released |

Different from text `input()` — events arrive each frame. You check the event queue inside the loop instead of waiting on one line of text.

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
```

## Colors

Pygame colors are RGB tuples — red, green, blue — each from 0 to 255:

```python
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
GRID_COLOR = (50, 50, 60)
BACKGROUND = (20, 20, 30)
```

`(255, 0, 0)` is pure red; `(0, 255, 0)` is green. Mix channels for grays and pastels. Store colors in constants or a dict keyed by piece letter — same idea as `COLORS` in the next chapter.

## Coordinate System

Top-left is `(0, 0)`. `x` increases right, `y` increases **down** — same as our board rows!

```
(0,0) ------> x
  |
  v
  y
```

Board row 0 draws at the top of the grid; row 19 near the bottom. Column 0 is the left wall. That match with your 2D list indexing is why Tetris maps cleanly to Pygame.

Pixel position from grid cell:

```python
CELL = 30
pixel_x = col * CELL
pixel_y = row * CELL
```

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgot `pygame.init()` | Black screen or errors | Call before `set_mode` |
| No `display.flip()` | Window stays blank | Flip after every draw |
| Install outside venv | Import works in terminal, not IDE | Activate venv; reinstall |
| Busy loop without clock | CPU at 100% | Use `clock.tick(60)` in real game |

## Try It Yourself

Change window size and background color. Draw one white rectangle with `pygame.draw.rect`:

```python
pygame.draw.rect(screen, (255, 255, 255), (100, 80, 50, 50))
# rectangle at x=100, y=80, width=50, height=50
```

Run the test script again. Experiment with different RGB values until the window looks how you want.

## Summary

- **`pip install pygame`** in venv; record in `requirements.txt`.
- **Event loop** polls input each frame; **`display.flip()`** refreshes screen.
- Colors are RGB tuples; grid `(row, col)` maps to pixel `(col * CELL, row * CELL)`.
- Next: **visual Tetris**.

**Next:** [Color Tetris with Graphics](02-visual-tetris.md)
