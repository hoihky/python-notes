---
title: Drawing the Grid in the Terminal
order: 4
---

# Chapter 30: Drawing the Grid in the Terminal

Polish the **visual** side: borders, score line, and a stable draw function before game logic.

## Enhanced draw_board

```python
from constants import WIDTH, HEIGHT, EMPTY

def draw_board(board, piece_cells=None, score=0, lines=0):
    display = [row[:] for row in board]
    if piece_cells:
        for r, c in piece_cells:
            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                display[r][c] = "#"

    print("\n" * 2)
    print("=" * (WIDTH + 2))
    print(f" Score: {score}   Lines: {lines}")
    print("+" + "-" * WIDTH + "+")
    for row in display:
        print("|" + "".join(row) + "|")
    print("+" + "-" * WIDTH + "+")
    print(" a:left  d:right  s:down  w:rotate  q:quit")
```

Borders help you **see** the playfield edges.

## Hide Cursor Flicker (Optional)

Some terminals flicker when clearing. Our `\n * 2` trick is simple. Advanced: ANSI escape codes — skip for now.

## draw_game State Function

```python
def draw_game(state):
    cells = get_cells(
        state["piece_row"],
        state["piece_col"],
        state["name"],
        state["rotation"],
    )
    draw_board(
        state["board"],
        cells,
        state["score"],
        state["lines"],
    )
```

Pass one **dictionary** `state` — preview before formal classes.

## Initialize State

```python
def new_game_state():
    name, rot, pr, pc = spawn_piece()
    return {
        "board": make_board(),
        "name": name,
        "rotation": rot,
        "piece_row": pr,
        "piece_col": pc,
        "score": 0,
        "lines": 0,
        "game_over": False,
    }
```

## Mini Demo Loop

```python
def demo():
    state = new_game_state()
    while not state["game_over"]:
        draw_game(state)
        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        if cmd == "s":
            state["piece_row"] += 1
    print("Bye!")

if __name__ == "__main__":
    demo()
```

Movement has **no collision** yet — next chapters fix that.

## Try It Yourself

Add display of current piece name: `Piece: T` in header.

## Summary

- **Borders** and **score** make play readable.
- **`state` dict** holds all game variables.
- Demo loop ties **draw → input → update**.
- Part 10 adds **real rules**.

**Next:** [Moving the Piece](../part10-tetris-logic/01-moving-pieces.html)
