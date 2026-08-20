# Chapter 31: Moving the Piece

Movement updates `piece_col` (left/right) or `piece_row` (down). We only apply a move if it stays **valid** — collision comes next chapter; here we add structure.

Think of the falling piece like a sticker you can slide around on a glass table. You propose a new position, check whether it fits, and only then commit the change. That "propose, check, commit" pattern is the heart of every Tetris move.

## What Changes When You Move?

Each piece has a **position** (`piece_row`, `piece_col`) and a **rotation** (0–3). Moving left or right changes the column. Moving down changes the row. Rotation does not change position — it swaps which shape offsets apply.

| Key | Action | Changes |
|-----|--------|---------|
| `a` | Left | `piece_col -= 1` |
| `d` | Right | `piece_col += 1` |
| `s` | Soft drop | `piece_row += 1` |
| `w` | Rotate | `rotation = (rotation + 1) % 4` |

The `% 4` keeps rotation in the range 0, 1, 2, 3. After rotation 3, the next rotation wraps back to 0.

## try_move Helper

Instead of changing position directly everywhere, we wrap the logic in one function. Every move goes through the same gate:

```python
def try_move(state, d_row, d_col):
    new_row = state["piece_row"] + d_row
    new_col = state["piece_col"] + d_col
    cells = get_cells(new_row, new_col, state["name"], state["rotation"])
    if can_place(state["board"], cells):
        state["piece_row"] = new_row
        state["piece_col"] = new_col
        return True
    return False
```

Why return `True` or `False`? Callers like gravity need to know whether the piece actually moved. If `try_move` returns `False`, gravity will eventually call `lock_piece` — the piece hit something below.

`can_place` is defined in the next chapter — for now assume it exists and returns `True` until you wire up walls and locked blocks.

### Step-by-step walkthrough

Suppose the piece is at row 5, column 4 and the player presses `d` (right):

1. `handle_input` calls `try_move(state, 0, 1)`.
2. `new_row = 5`, `new_col = 5`.
3. `get_cells` returns the four board coordinates the piece would occupy.
4. `can_place` checks those cells — if all clear, update state and return `True`.
5. If blocked, state stays unchanged and return `False`.

The old position is never lost because we only write to `state` after the check passes.

## Handle Commands

Map keyboard letters to move attempts:

```python
def handle_input(state, cmd):
    if cmd == "a":
        try_move(state, 0, -1)
    elif cmd == "d":
        try_move(state, 0, 1)
    elif cmd == "s":
        try_move(state, 1, 0)
    elif cmd == "w":
        try_rotate(state)
    elif cmd == "q":
        state["game_over"] = True
```

Notice that invalid moves are silent — the piece simply does not move. That matches real Tetris: pressing left against a wall does nothing harmful.

You can test input without a full game loop:

```python
state = {"piece_row": 10, "piece_col": 4, "name": "T", "rotation": 0, "board": make_board(), "game_over": False}
handle_input(state, "d")
print(state["piece_col"])  # 5 if can_place returned True
```

## Rotation

Rotation uses the same validate-then-commit pattern as sliding:

```python
def try_rotate(state):
    new_rot = (state["rotation"] + 1) % 4
    cells = get_cells(
        state["piece_row"], state["piece_col"],
        state["name"], new_rot
    )
    if can_place(state["board"], cells):
        state["rotation"] = new_rot
```

Each shape in `SHAPES` has four lists of offsets — one per rotation. When rotation changes, `get_cells` reads different offsets but the anchor row/col stay the same.

### Mini demo: rotation in numbers

```python
state = {"piece_row": 2, "piece_col": 3, "name": "O", "rotation": 0}
try_rotate(state)
print(state["rotation"])  # 1
try_rotate(state)
print(state["rotation"])  # 2
# After four rotates, back to 0
```

## Soft Drop vs Gravity

**Soft drop** (`s` key): player pushes the piece down one row immediately.

**Gravity**: the piece falls on its own, like real Tetris.

Each loop iteration can follow this order:

1. Player moves (optional key press)
2. Piece falls one row automatically (classic Tetris)

```python
def tick_gravity(state):
    if not try_move(state, 1, 0):
        lock_piece(state)  # chapter 33
```

When `try_move(state, 1, 0)` fails, the piece cannot go lower — it locks in place. That connection between failed downward move and locking is central to the whole game.

Text version note: gravity happens **after** each key press in our simple loop. A fancier version would auto-fall every N turns or use a timer (Pygame does this in Part 12).

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
| Updating row/col before checking | Piece overlaps walls or locked blocks | Always compute `new_row`/`new_col`, validate, then assign |
| Forgetting to undo on failed rotate | Piece spins inside a wall | Only set `rotation` after `can_place` passes |
| Moving in `draw_board` | Board data gets corrupted | Drawing reads state; only `try_move` writes position |
| Using separate logic for each direction | Copy-paste bugs | One `try_move(state, d_row, d_col)` handles all slides |

## Try It Yourself

Wire `handle_input` into your demo loop. Confirm `a`/`d`/`s` change position when `can_place` always returns True (temporary stub):

```python
def can_place(board, cells):
    return True  # stub — replace in next chapter

# In your loop:
draw_game(state)
cmd = input("> ").strip().lower()
handle_input(state, cmd)
tick_gravity(state)
```

Print `piece_row` and `piece_col` after each turn until the behavior feels predictable.

## Summary

- Movement = change row/col **if valid**.
- Rotation cycles **0–3** using `% 4`.
- **`try_move`** centralizes all slide attempts and returns whether the move succeeded.
- Failed downward move → lock (next chapter).
- Next: **`can_place`** collision detection.

**Next:** [Collision Detection](02-collision-detection.md)
