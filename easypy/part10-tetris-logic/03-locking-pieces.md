---
title: Locking Pieces on the Board
order: 3
---

# Chapter 33: Locking Pieces on the Board

When a piece can no longer move down, it **locks** — its cells merge into `board` and become permanent.

## lock_piece

```python
from constants import BLOCK

def lock_piece(state):
    cells = get_cells(
        state["piece_row"], state["piece_col"],
        state["name"], state["rotation"]
    )
    for row, col in cells:
        if row >= 0:
            state["board"][row][col] = BLOCK
    spawn_new_piece(state)
```

After lock, spawn next piece (from collision chapter).

## tick_gravity with Lock

```python
def tick_gravity(state):
    if try_move(state, 1, 0):
        return  # moved down OK
    lock_piece(state)
```

## Hard Drop (Optional)

```python
def hard_drop(state):
    while try_move(state, 1, 0):
        pass
    lock_piece(state)
```

Map to key `space` later in Pygame.

## Order of Operations Each Turn

```python
def game_tick(state, cmd):
    if cmd:
        handle_input(state, cmd)
    if not state["game_over"]:
        tick_gravity(state)
        clear_full_lines(state)  # next chapter
```

Adjust if you want gravity only on empty input.

## Try It Yourself

Play until piece lands. Print board — locked cells should stay after new piece spawns.

## Summary

- **Lock** copies piece cells into `board`.
- **Gravity** then **lock** when blocked.
- **Spawn** new piece after lock.
- Next: **clear full lines**.

**Next:** [Clearing Full Lines](04-clearing-lines.html)
