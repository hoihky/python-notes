# Chapter 35: Score and Game Over

Put everything in **`tetris.py`** — a playable text Tetris game.

This chapter is the assembly step. You already wrote movement, collision, locking, and line clears in pieces. Now connect them into one loop a human can play from the terminal.

## Complete Main Loop

The loop follows the same rhythm every turn: show state, read input, apply physics, clean up lines, repeat until game over.

```python
from board import make_board, draw_board
from game_logic import (
    new_game_state, draw_game, handle_input,
    tick_gravity, clear_full_lines,
)

def main():
    state = new_game_state()
    print("Welcome to Text Tetris!")
    print("Controls: a/d move, s drop, w rotate, q quit")

    while not state["game_over"]:
        draw_game(state)
        cmd = input("> ").strip().lower()
        handle_input(state, cmd)
        if not state["game_over"]:
            tick_gravity(state)
            clear_full_lines(state)

    draw_game(state)
    print(f"Game Over! Final score: {state['score']}")

if __name__ == "__main__":
    main()
```

Organize helpers in `game_logic.py` as you prefer — one file for logic, one for drawing, one for shapes keeps imports readable.

### What happens each iteration

1. **`draw_game`** — print board with falling piece overlaid (on a copy, not mutating locked cells).
2. **`input`** — wait for player command.
3. **`handle_input`** — move, rotate, or quit.
4. **`tick_gravity`** — auto-fall or lock.
5. **`clear_full_lines`** — remove completed rows and add score.

If the player quits with `q`, skip gravity on that turn so the game ends immediately without an extra lock.

## game_over Conditions

Two paths end the game:

1. New piece cannot spawn (`spawn_new_piece` sets flag) — stack reached the top.
2. Player presses `q` — voluntary quit.

There is no timer in the text version unless you add one. Game over is always deterministic from board state or player choice.

```python
# Inside spawn_new_piece, after can_place fails:
state["game_over"] = True
# Player sees final board and score message
```

## Show Final Stats

Give the player closure with more than just score:

```python
print(f"Lines cleared: {state['lines']}")
print(f"Score: {state['score']}")
if state["lines"] >= 4:
    print("Nice work — you cleared multiple lines!")
```

Optional: compare to a personal best stored in a file (see Try It Yourself).

## Suggested project layout

| File | Role |
|------|------|
| `constants.py` | WIDTH, HEIGHT, EMPTY, BLOCK |
| `shapes.py` | SHAPES, PIECE_LETTERS, get_cells |
| `board.py` | make_board, draw_board |
| `game_logic.py` | state, input, gravity, lock, clear |
| `tetris.py` | main loop only |

Keeping `tetris.py` thin makes it obvious where execution starts.

## Playtest Checklist

| Test | Expected |
|------|----------|
| Move left/right | Stops at walls |
| Soft drop | Locks at bottom or stack |
| Fill row | Row disappears, score up |
| Stack to top | Game over |
| Press q mid-game | Loop exits, stats print |
| Rotate near wall | Piece does not clip through |
| Spawn after lock | New random piece appears |

Run through the checklist once after every big change. Regressions are easier to catch with a fixed list than random play alone.

## Common Bugs

| Bug | Fix |
|-----|-----|
| Piece erases locked blocks | Draw on copy only — never write falling cells into `board` until lock |
| Ghost piece on board | Don't write falling cells to `board` until lock |
| Index error | Check bounds in `can_place` |
| Rotation through walls | `can_place` rejects bad rotation |
| Double gravity | Call `tick_gravity` once per loop iteration |
| Score never changes | Call `clear_full_lines` after lock |
| Game never ends | Verify spawn check sets `game_over` |

## Celebrate

You built a real game with **variables, loops, lists, functions, and logic**. The rules are the same ones commercial Tetris implements — you just expressed them in text. Take a screenshot of your terminal!

From here, Part 11 reorganizes the same ideas with classes. Part 12 draws them with Pygame. The logic you wrote now carries forward.

## Try It Yourself

Add `h` command for hard drop. Add high score saved to a text file:

```python
def save_high_score(score):
    try:
        with open("highscore.txt") as f:
            best = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        best = 0
    if score > best:
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print(f"New high score: {score}!")

# Call save_high_score(state["score"]) after game over
```

Track how many pieces you locked in a session, or print a hint when the stack passes half height.

## Summary

- **Main loop**: draw → input → gravity → clear lines.
- **Game over** on quit or blocked spawn.
- Split code across modules; keep main loop readable.
- You have **playable text Tetris**!
- Next: **classes** to organize code.

**Next:** [Introduction to Classes and Objects](../part11-classes/01-objects-and-classes.md)
