# Chapter 14: Updating and Displaying Values

Games **change** every frame: position updates, score rises. This chapter practices **read → change → show** — the heartbeat of Tetris.

Every tick of the game loop follows the same rhythm: read current state, apply rules (move, rotate, lock), write new state, show the player what happened. Variables are how you remember state between ticks.

## Track State with Variables

```python
score = 0
lines_cleared = 0
piece_x = 4
piece_y = 0
game_over = False
```

**State** = everything needed to describe the game right now. If you saved these five values to a file and restored them later, you could resume the same match (we will not do that yet — but the idea matters).

| Variable | Role in Tetris |
|----------|----------------|
| `score` | Points earned so far |
| `lines_cleared` | Total lines removed |
| `piece_x`, `piece_y` | Active piece position |
| `game_over` | Whether the loop should stop |

## Display State

```python
score = 0
lines_cleared = 0
piece_x = 4
piece_y = 0

print("--- Tetris ---")
print(f"Score: {score}")
print(f"Lines: {lines_cleared}")
print(f"Piece at column {piece_x}, row {piece_y}")
```

Expected output:

```
--- Tetris ---
Score: 0
Lines: 0
Piece at column 4, row 0
```

Using f-strings keeps labels and values together. When score changes, re-print — the screen (or terminal) shows the latest numbers.

## Simulate One “Tick”

```python
piece_y = 0
print(f"Before fall: row {piece_y}")  # expected output: Before fall: row 0

# Piece falls one row
piece_y += 1
print(f"After fall: row {piece_y}")   # expected output: After fall: row 1
```

Gravity in Tetris is just `piece_y += 1` repeated on a timer or each loop pass. No magic — one variable steps downward.

## Simulate Clearing a Line

```python
score = 0
lines_cleared = 0

lines_cleared += 1
score += 100
print(f"Score: {score}, Lines: {lines_cleared}")
# expected output: Score: 100, Lines: 1

lines_cleared += 1
score += 100
print(f"Score: {score}, Lines: {lines_cleared}")
# expected output: Score: 200, Lines: 2
```

Real Tetris uses tiered scoring (single, double, triple, Tetris). For now, flat `+100` per line keeps the pattern obvious: **event happens → variables update → print**.

## Update Several Values in One Turn

```python
piece_y = 18
score = 400
lines_cleared = 3
game_over = False

# Piece locks at bottom row
piece_y += 1
lines_cleared += 1
score += 100

if piece_y >= 19:
    game_over = True

print(f"y={piece_y}, score={score}, lines={lines_cleared}, over={game_over}")
# expected output: y=19, score=500, lines=4, over=True
```

One turn can touch many variables. Order matters when later lines depend on earlier updates — here we move, score, then check game over.

## Clear Screen (Simple Trick)

Text Tetris redraws the board each turn. Minimal approach:

```python
print("\n" * 30)  # many blank lines — crude clear
print("--- Tetris ---")
print("Score: 100")
```

Terminals vary; later we redraw the full grid. The goal is the same: **show fresh state**, not append forever so the player scrolls up to find the board.

## Putting It Together — Mini Loop Preview

```python
piece_y = 0
while piece_y < 5:
    print(f"Piece at row {piece_y}")
    piece_y += 1
```

Expected output:

```
Piece at row 0
Piece at row 1
Piece at row 2
Piece at row 3
Piece at row 4
```

Full `while` explanation comes next part — this shows **why** we update variables in a loop. Each pass reads `piece_y`, prints it, adds 1, and checks again.

## Debug Habit — Print What You Think You Changed

When movement feels wrong, print immediately after assignment:

```python
piece_x = 4
piece_x += 1
print(f"DEBUG piece_x is now {piece_x}")  # expected output: DEBUG piece_x is now 5
```

Remove debug prints once behavior is correct — but while learning, they save hours.

## Common Mistakes

**Printing before updating**

```python
piece_y = 3
print(f"Row {piece_y}")  # shows 3
piece_y += 1
# forgot to print again — player still thinks row is 3
```

**Updating a copy of state in your head**

```python
score = 100
# you intend +50 but write:
score = 50   # overwrites instead of adding
# wanted: score += 50
```

**Stale display**

If you only print once at program start, the player never sees score rise. Re-print (or redraw) after each change that matters.

## Try It Yourself

Write `state_demo.py`:

1. Start `score=0`, `level=1`.
2. Add 100 to score three times (use `+=`).
3. Each time score passes 300, increase `level` by 1 (manual `if` for now: `if score >= 300: level = 2`).
4. Print final score and level.

Expected final output (approximately): `score` is 300, `level` is 2. Print after each `+=` to watch level bump when you cross the threshold.

## Summary

- **State variables** describe the game moment — position, score, flags.
- **Update** then **print** to see changes; games loop that pair forever.
- Tetris repeats: move → draw → check lines → repeat.
- Debug prints right after assignment catch off-by-one bugs early.
- Next: **decisions** with `if`.

**Next:** [True, False, and Comparisons](../part5-decisions/01-boolean-logic.md)
