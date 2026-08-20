# Chapter 32: Collision Detection

**Collision** means: "Would this block overlap a wall, floor, or locked `#`?"

Imagine sliding a couch through a doorway. It fits only if every corner clears the frame and nothing is already in the way. Tetris uses the same idea: we list every cell the piece would cover, then ask whether each cell is legal.

## can_place

This function is the gatekeeper for every move and rotation:

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

Read it as a checklist for each cell `(row, col)`:

1. Is the column outside the left or right wall? → reject.
2. Is the row below the floor? → reject.
3. Is the row above the visible top? → skip (still falling in).
4. Is the board cell already filled? → reject.
5. All cells passed → allow.

If any check fails, we return `False` immediately. That is called **early exit** — no need to keep checking once we know the move is illegal.

## Why row < 0 Is OK

Pieces spawn partly above visible grid. We allow negative rows until they enter play.

When a new piece appears, one or two blocks may sit at row -1 or -2 — above what you see on screen. That is normal. We only reject cells that fall **below** the board (`row >= HEIGHT`) or **sideways** out of bounds. Cells above row 0 are ignored until they drop into view.

```python
# Piece partly above the top — still valid
cells = [(-1, 4), (-1, 5), (0, 4), (0, 5)]
print(can_place(make_board(), cells))  # True
```

Once those cells reach row 0 and below, they must land on empty spaces like any other block.

## Wall Tests

| Move | Failure when |
|------|--------------|
| Left | any cell col < 0 |
| Right | any cell col >= WIDTH |
| Down | any cell row >= HEIGHT OR cell not empty |

Walls are **hard** boundaries — the piece never wraps around. The floor is row `HEIGHT - 1` (index 19 in a 20-row board), but we detect floor contact by checking `row >= HEIGHT` on the cell **below** the piece, or by finding a non-empty cell directly underneath.

## Floor = Locked Blocks

When down move fails because `board[row][col]` is not empty, piece **locks** (next chapter).

Locked blocks act like a custom floor built by the player. A piece might legally be at row 10, but if row 11 beneath it contains `#`, moving down fails even though row 11 is not the bottom of the board.

```python
board = make_board()
board[15][5] = "#"  # a stack of blocks
cells_below = [(16, 5), (16, 6), (15, 5), (15, 6)]
print(can_place(board, cells_below))  # False — overlaps the #
```

## Testing can_place in isolation

Before connecting to movement, verify collision logic with small examples:

```python
def test_collision():
    b = make_board()
    b[19][5] = "#"  # block on bottom
    cells = [(19, 5), (19, 6), (18, 5), (18, 6)]
    assert can_place(b, cells) == False
    cells_ok = [(18, 4), (18, 5), (17, 4), (17, 5)]
    assert can_place(b, cells_ok) == True
    print("All collision tests passed")

test_collision()
# expected output: All collision tests passed
```

Run tests manually with `assert` or print `can_place(...)` before and after placing blocks. When an assert fails, Python tells you the line number — follow it back to the logic that broke.

## Spawn Check — Game Over

Collision also decides whether a **new** game can continue:

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

This is the classic "stack reached the top" ending. Even one blocked cell at spawn means there is no room left. The player might never see the new piece — the game ends on the lock that caused the overlap.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Rejecting `row < 0` | Piece disappears at spawn | Use `continue` for negative rows |
| Checking `row < 0` for walls | Confusing top with left/right | Only `col` checks use `< 0` and `>= WIDTH` |
| Comparing to wrong empty symbol | Collisions never detected | Use `EMPTY` from constants, not hard-coded `"."` |
| Forgetting spawn check | Game continues with overlapping pieces | Call `can_place` in `spawn_new_piece` |

## Debugging tip: print the cells

When a move feels wrong, log what you are testing:

```python
cells = get_cells(state["piece_row"], state["piece_col"], state["name"], state["rotation"])
print("Testing cells:", cells, "→", can_place(state["board"], cells))
```

Compare printed coordinates to your drawn board. Off-by-one errors in `get_cells` show up immediately.

## Try It Yourself

Place `#` on board. Verify piece cannot move into it. Print `can_place` before/after each attempted move:

```python
state = new_game_state()
state["board"][12][5] = "#"
draw_game(state)
print(can_place(state["board"], get_cells(state["piece_row"], state["piece_col"], state["name"], state["rotation"])))
try_move(state, 0, -1)
print("After left:", state["piece_col"])
```

Build a small stack near the center and try to rotate into it — rotation should fail cleanly with no state change.

## Summary

- **`can_place`** checks bounds and empty cells for every block in the piece.
- Negative rows allowed for spawning; negative columns are not.
- Locked `#` cells block movement the same way walls do.
- Failed spawn = **game over** (top out).
- Next: **locking** piece to board.

**Next:** [Locking Pieces on the Board](03-locking-pieces.md)
