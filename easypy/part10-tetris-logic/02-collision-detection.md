---
title: Collision Detection
order: 2
---

# Chapter 32: Collision Detection

**Collision** means: “Would this block overlap a wall, floor, or locked `#`?”

## can_place

```python
from constants import HEIGHT, WIDTH, EMPTY

def can_place(board, cells):
    for row, col in cells:
        # Out of bounds = not allowed
        if col < 0 or col >= WIDTH or row >= HEIGHT:
            return False
        # Above top (row < 0) is OK while falling
        if row < 0:
            continue
        if board[row][col] != EMPTY:
            return False
    return True
```

## Why row < 0 Is OK

Pieces spawn partly above visible grid. We allow negative rows until they enter play.

## Wall Tests

| Move | Failure when |
|------|--------------|
| Left | any cell col < 0 |
| Right | any cell col >= WIDTH |
| Down | any cell row >= HEIGHT OR cell not empty |

## Floor = Locked Blocks

When down move fails because `board[row][col]` is not empty, piece **locks** (next chapter).

## Test Cases

```python
def test_collision():
    b = make_board()
    b[19][5] = "#"  # block on bottom
    cells = [(19, 5), (19, 6), (18, 5), (18, 6)]
    assert can_place(b, cells) == False
    cells_ok = [(18, 4), (18, 5), (17, 4), (17, 5)]
    assert can_place(b, cells_ok) == True
```

Run tests manually or with `assert`.

## Spawn Check — Game Over

```python
def spawn_new_piece(state):
    name, rot, pr, pc = spawn_piece()
    cells = get_cells(pr, pc, name, rot)
    if not can_place(state["board"], cells):
        state["game_over"] = True
        return
    state["name"] = name
    state["rotation"] = rot
    state["piece_row"] = pr
    state["piece_col"] = pc
```

If new piece collides immediately → **top out** → game over.

## Try It Yourself

Place `#` on board. Verify piece cannot move into it. Print `can_place` before/after.

## Summary

- **`can_place`** checks bounds and empty cells.
- Negative rows allowed for spawning.
- Failed spawn = **game over**.
- Next: **locking** piece to board.

**Next:** [Locking Pieces on the Board](03-locking-pieces.html)
