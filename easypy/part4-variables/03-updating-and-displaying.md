---
title: Updating and Displaying Values
order: 3
---

# Chapter 14: Updating and Displaying Values

Games **change** every frame: position updates, score rises. This chapter practices **read → change → show** — the heartbeat of Tetris.

## Track State with Variables

```python
score = 0
lines_cleared = 0
piece_x = 4
piece_y = 0
game_over = False
```

**State** = everything needed to describe the game right now.

## Display State

```python
print("--- Tetris ---")
print(f"Score: {score}")
print(f"Lines: {lines_cleared}")
print(f"Piece at column {piece_x}, row {piece_y}")
```

## Simulate One “Tick”

```python
# Piece falls one row
piece_y += 1
print(f"After fall: row {piece_y}")
```

## Simulate Clearing a Line

```python
lines_cleared += 1
score += 100
print(f"Score: {score}, Lines: {lines_cleared}")
```

## Clear Screen (Simple Trick)

Text Tetris redraws the board each turn. Minimal approach:

```python
print("\n" * 30)  # many blank lines — crude clear
```

Terminals vary; later we redraw the full grid.

## Putting It Together — Mini Loop Preview

```python
piece_y = 0
while piece_y < 5:
    print(f"Piece at row {piece_y}")
    piece_y += 1
```

Full `while` explanation comes next part — this shows **why** we update variables in a loop.

## Try It Yourself

Write `state_demo.py`:

1. Start `score=0`, `level=1`.
2. Add 100 to score three times (use `+=`).
3. Each time score passes 300, increase `level` by 1 (manual `if` for now: `if score >= 300: level = 2`).
4. Print final score and level.

## Summary

- **State variables** describe the game moment.
- **Update** then **print** to see changes.
- Tetris repeats: move → draw → check lines → repeat.
- Next: **decisions** with `if`.

**Next:** [True, False, and Comparisons](../part5-decisions/01-boolean-logic.html)
