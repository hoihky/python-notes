---
title: Score and Game Over
order: 5
---

# Chapter 35: Score and Game Over

Put everything in **`tetris.py`** — a playable text Tetris game.

## Complete Main Loop

```python
from board import make_board, draw_board
from game_logic import (
    new_game_state, draw_game, handle_input,
    tick_gravity, clear_full_lines,
)

def main():
    state = new_game_state()
    print("Welcome to Text Tetris!")

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

Organize helpers in `game_logic.py` as you prefer.

## game_over Conditions

1. New piece cannot spawn (`spawn_new_piece` sets flag)
2. Player presses `q`

## Show Final Stats

```python
print(f"Lines cleared: {state['lines']}")
print(f"Score: {state['score']}")
```

## Playtest Checklist

| Test | Expected |
|------|----------|
| Move left/right | Stops at walls |
| Soft drop | Locks at bottom or stack |
| Fill row | Row disappears, score up |
| Stack to top | Game over |

## Common Bugs

| Bug | Fix |
|-----|-----|
| Piece erases locked blocks | Draw on copy only |
| Ghost piece on board | Don't write falling cells to `board` until lock |
| Index error | Check bounds in `can_place` |
| Rotation through walls | `can_place` rejects bad rotation |

## Celebrate

You built a real game with **variables, loops, lists, functions, and logic**. Take a screenshot of your terminal!

## Try It Yourself

Add `h` command for hard drop. Add high score saved to a text file.

## Summary

- **Main loop**: draw → input → gravity → clear lines.
- **Game over** on quit or blocked spawn.
- You have **playable text Tetris**!
- Next: **classes** to organize code.

**Next:** [Introduction to Classes and Objects](../part11-classes/01-objects-and-classes.html)
