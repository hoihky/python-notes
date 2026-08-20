# Chapter 34: Clearing Full Lines

When a row has **no empty cells**, remove it and push everything above **down**.

Line clears are Tetris at its most satisfying. You built a messy stack, one row became completely full, and the board **heals** — that row vanishes and everything above slides down one step. Your score jumps too.

## is_row_full

Start with a simple question per row: is there any empty cell left?

```python
from constants import EMPTY, WIDTH

def is_row_full(row):
    return EMPTY not in row
```

A row is a list of characters (or symbols). If `.` (or whatever `EMPTY` is) appears anywhere, the row is incomplete. If every slot is `#` or a block character, the row is full.

```python
full = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
gap = [".", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
print(is_row_full(full))  # True
print(is_row_full(gap))   # False
```

## clear_full_lines

Build a new board without full rows, then pad empty rows at the top:

```python
from constants import HEIGHT, EMPTY, WIDTH

def clear_full_lines(state):
    board = state["board"]
    new_board = []
    cleared = 0
    for row in board:
        if is_row_full(row):
            cleared += 1
        else:
            new_board.append(row)
    while len(new_board) < HEIGHT:
        new_board.insert(0, [EMPTY] * WIDTH)
    state["board"] = new_board
    if cleared:
        state["lines"] += cleared
        POINTS = {1: 100, 2: 300, 3: 500, 4: 800}
        state["score"] += POINTS.get(cleared, cleared * 100)
```

### Walkthrough: two rows cleared at once

Suppose rows 18 and 19 are both full, and rows 0–17 have gaps:

1. Loop skips rows 18 and 19 (both full) — `cleared` becomes 2.
2. `new_board` holds rows 0–17 (18 rows).
3. `while len(new_board) < HEIGHT` inserts two fresh empty rows at index 0.
4. Final board still has 20 rows; stack sits lower; top has new empty space.

Insert empty rows at **top** to replace removed ones. New empty space appears above the stack, matching how Tetris feels — blocks fall into the gap left behind.

## Why build a new list?

You could delete rows in place, but rebuilding is clearer for beginners:

- Scan old board top to bottom.
- Keep incomplete rows in order.
- Pad until height matches `HEIGHT`.

No index shifting bugs from deleting while iterating.

## Scoring Ideas

Clearing more lines at once rewards planning:

| Lines at once | Points (example) | Name |
|---------------|------------------|------|
| 1 | 100 | Single |
| 2 | 300 | Double |
| 3 | 500 | Triple |
| 4 (Tetris!) | 800 | Tetris |

The `{1: 100, 2: 300, ...}` dict gives bonus points for multi-line clears. Real Tetris games use similar escalating tables. You can tune numbers for your own difficulty.

```python
# Quick score check
state = {"board": make_board(), "lines": 0, "score": 0}
state["board"][19] = [BLOCK] * WIDTH  # fill bottom row manually
clear_full_lines(state)
print(state["lines"], state["score"])  # 1 100
```

## When to call clear_full_lines

Call it **after** lock, when new blocks might have completed a row:

```python
def tick_gravity(state):
    if try_move(state, 1, 0):
        return
    lock_piece(state)
    clear_full_lines(state)  # if not already in game_tick
```

If you already call it in `game_tick`, do not call it twice — double clearing would be a bug.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Appending empty rows at bottom | Stack floats wrong | Use `insert(0, ...)` at top |
| Wrong row count after clear | Index errors later | Loop until `len(new_board) == HEIGHT` |
| Treating almost-full row as full | Row never clears | Check `EMPTY not in row`, not cell count |
| Clearing before lock | Piece cells missing from row | Run clear after piece is written to board |

## Visual Test

Fill bottom row manually with `#`, call `clear_full_lines`, draw — row should empty and stack shift:

```python
state = new_game_state()
state["board"][19] = ["#"] * WIDTH
print("Before:", sum(is_row_full(r) for r in state["board"]))  # 1
clear_full_lines(state)
print("After:", sum(is_row_full(r) for r in state["board"]))   # 0
draw_game(state)
```

Fill rows 18 and 19 together to test a double clear — `lines` should increase by 2 and score by 300 with the example table.

## Try It Yourself

Clear two rows at once. Check `lines` and `score` update:

```python
state = new_game_state()
state["board"][18] = ["#"] * WIDTH
state["board"][19] = ["#"] * WIDTH
clear_full_lines(state)
print(f"Lines: {state['lines']}, Score: {state['score']}")
# expected: Lines: 2, Score: 300
```

Try a triple line setup (rows 17–19 full) and confirm the 500-point bonus.

## Summary

- **Full row** = no `.` (empty) left in that row.
- Remove full rows, add empty rows on **top**, keep height constant.
- Update **score** and **lines cleared** with bonus for multi-line clears.
- Call after locking so completed rows include the piece that just landed.
- Next: **game over** and full **main**.

**Next:** [Score and Game Over](05-score-and-game-over.md)
