---
title: Clearing Full Lines
order: 4
---

# Chapter 34: Clearing Full Lines

When a row has **no empty cells**, remove it and push everything above **down**.

## is_row_full

```python
from constants import EMPTY, WIDTH

def is_row_full(row):
    return EMPTY not in row
```

## clear_full_lines

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

Insert empty rows at **top** to replace removed ones.

## Scoring Ideas

| Lines at once | Points (example) |
|---------------|------------------|
| 1 | 100 |
| 2 | 300 |
| 3 | 500 |
| 4 (Tetris!) | 800 |

## Visual Test

Fill bottom row manually with `#`, call `clear_full_lines`, draw — row should empty and stack shift.

## Try It Yourself

Clear two rows at once. Check `lines` and `score` update.

## Summary

- **Full row** = no `.` left.
- Remove rows, add empty rows on top.
- Update **score** and **lines cleared**.
- Next: **game over** and full **main**.

**Next:** [Score and Game Over](05-score-and-game-over.html)
