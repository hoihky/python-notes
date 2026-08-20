# Chapter 30: Drawing the Grid in the Terminal

Polish the **visual** side: borders, score line, and a stable draw function before game logic.

Raw rows of dots work for learning, but players lose track of edges and score. A simple ASCII frame — plus labels — makes text Tetris feel like a real game window. Logic stays the same; only presentation improves.

## Enhanced draw_board

```python
from constants import WIDTH, HEIGHT, EMPTY, BLOCK

def draw_board(board, piece_cells=None, score=0, lines=0, piece_name=""):
    display = [row[:] for row in board]
    if piece_cells:
        for r, c in piece_cells:
            if 0 <= r < HEIGHT and 0 <= c < WIDTH:
                display[r][c] = BLOCK

    print("\n" * 2)
    print("=" * (WIDTH + 2))
    header = f" Score: {score}   Lines: {lines}"
    if piece_name:
        header += f"   Piece: {piece_name}"
    print(header)
    print("+" + "-" * WIDTH + "+")
    for row in display:
        print("|" + "".join(row) + "|")
    print("+" + "-" * WIDTH + "+")
    print(" a:left  d:right  s:down  w:rotate  q:quit")
```

Borders help you **see** the playfield edges.

Walkthrough of one frame:

1. Copy board → overlay falling cells on copy.
2. Print separator line (`=`).
3. Print score, lines, optional piece name.
4. Print top border `+----------+`.
5. Each row wrapped in `| ... |`.
6. Print bottom border and control hints.

Using `BLOCK` from constants keeps symbols consistent with locked blocks on the board.

## Sample Output Shape

```
========================================
 Score: 0   Lines: 0   Piece: T
+----------+
|....##....|
|...####...|
|..........|
+----------+
 a:left  d:right  s:down  w:rotate  q:quit
```

Exact dots depend on your piece — the **frame** is what matters.

## Hide Cursor Flicker (Optional)

Some terminals flicker when clearing. Our `\n * 2` trick is simple — scroll old frames up instead of erasing the screen. Advanced: ANSI escape codes to move cursor home — skip for now unless flicker bothers you.

For learning, readability beats perfect animation.

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
        state["name"],
    )
```

Pass one **dictionary** `state` — preview before formal classes.

Benefits of a state dict:

- One argument carries board, piece, score — fewer parameters to reorder by mistake.
- Easy to print debug: `print(state.keys())`.
- Later, swap dict for a small class if you prefer — same fields.

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

Every key the loop needs starts here. **`game_over`** flips when spawn fails — loop condition checks it.

## Mini Demo Loop

```python
def demo():
    state = new_game_state()
    while not state["game_over"]:
        draw_game(state)
        cmd = input("> ").strip().lower()
        if cmd == "q":
            break
        if cmd == "a":
            state["piece_col"] -= 1
        if cmd == "d":
            state["piece_col"] += 1
        if cmd == "s":
            state["piece_row"] += 1
    print("Bye!")

if __name__ == "__main__":
    demo()
```

Movement has **no collision** yet — next chapters fix that.

Try the demo:

1. `python3 tetris.py` (or your main file).
2. Press `d` several times — piece shifts right on screen, board still empty underneath.
3. Press `s` — piece moves down.
4. Press `q` — clean exit.

That proves **draw → input → update** wiring before rules.

## Soft Drop vs Display

Each `s` increases `piece_row`. Without collision, piece sinks through blocks and floor — expected for now. Part 10 adds `can_place` so downward moves stop at the bottom and locked cells.

## Common Mistakes

| Mistake | What happens | Fix |
|---------|--------------|-----|
| Draw without copying board | Trails of `#` | Always overlay on `display` copy |
| Forgetting `.strip().lower()` on input | `"D"` ignored | Normalize input |
| Updating state but not redrawing | Screen stale | Draw at start of loop body |
| Missing `game_over` check | Infinite loop after lose | Set flag when spawn blocked |

## Try It Yourself

Add display of current piece name: `Piece: T` in header (shown in enhanced `draw_board` above).

**Bonus:** Show rotation number `Rot: 2` for debugging rotations. **Bonus 2:** Refuse moves that leave `piece_col < 0` using `max(0, col)` as a tiny wall test before full collision.

## Summary

- **Borders** and **score** make play readable.
- **`state` dict** holds all game variables.
- Demo loop ties **draw → input → update**.
- Presentation layer separate from board data — keep it that way.
- Part 10 adds **real rules**.

**Next:** [Moving the Piece](../part10-tetris-logic/01-moving-pieces.md)
