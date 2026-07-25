---
title: Moving the Piece
order: 1
---

# Chapter 31: Moving the Piece

Movement updates `piece_col` (left/right) or `piece_row` (down). We only apply a move if it stays **valid** — collision comes next chapter; here we add structure.

## try_move Helper

```python
def try_move(state, d_row, d_col):
    new_row = state["piece_row"] + d_row
    new_col = state["piece_col"] + d_col
    cells = get_cells(new_row, new_col, state["name"], state["rotation"])
    if can_place(state["board"], cells):
        state["piece_row"] = new_row
        state["piece_col"] = new_col
        return True
    return False
```

`can_place` defined in next chapter — for now assume it exists.

## Handle Commands

```python
def handle_input(state, cmd):
    if cmd == "a":
        try_move(state, 0, -1)
    elif cmd == "d":
        try_move(state, 0, 1)
    elif cmd == "s":
        try_move(state, 1, 0)
    elif cmd == "w":
        try_rotate(state)
    elif cmd == "q":
        state["game_over"] = True
```

## Rotation

```python
def try_rotate(state):
    new_rot = (state["rotation"] + 1) % 4
    cells = get_cells(
        state["piece_row"], state["piece_col"],
        state["name"], new_rot
    )
    if can_place(state["board"], cells):
        state["rotation"] = new_rot
```

## Soft Drop vs Gravity

Each loop iteration:

1. Player moves (optional)
2. Piece falls one row automatically (classic Tetris)

```python
def tick_gravity(state):
    if not try_move(state, 1, 0):
        lock_piece(state)  # chapter 33
```

Text version: gravity happens **after** each key press, or add auto-fall every N turns.

## Try It Yourself

Wire `handle_input` into your demo loop. Confirm `a`/`d`/`s` change position when `can_place` always returns True (temporary stub).

## Summary

- Movement = change row/col **if valid**.
- Rotation cycles **0–3**.
- **`try_move`** centralizes attempts.
- Next: **`can_place`** collision detection.

**Next:** [Collision Detection](02-collision-detection.html)
