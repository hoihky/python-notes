# Chapter 33: Locking Pieces on the Board

When a piece can no longer move down, it **locks** — its cells merge into `board` and become permanent.

Locking is the moment a falling shape becomes part of the landscape. Until then, the piece is a guest on the board — drawn on top but not stored in `board`. After lock, those cells are `#` (or `BLOCK`) forever, until a line clear removes them.

## lock_piece

```python
from constants import BLOCK

def lock_piece(state):
    cells = get_cells(
        state["piece_row"], state["piece_col"],
        state["name"], state["rotation"]
    )
    for row, col in cells:
        if row >= 0:
            state["board"][row][col] = BLOCK
    spawn_new_piece(state)
```

Two important details:

1. **`if row >= 0`** — skip cells still above the visible grid. They never touched the board, so there is nothing to write.
2. **`spawn_new_piece`** runs immediately after lock. The player always has a piece to control (unless spawn fails → game over).

After lock, the old piece no longer exists as a separate thing. Only the board remembers it.

### What locking does NOT do

Locking does not clear lines or update score — that comes next chapter. It also does not reset the board. It only paints four (or fewer for some shapes) cells and spawns the next piece.

## tick_gravity with Lock

Gravity and lock work as a pair:

```python
def tick_gravity(state):
    if try_move(state, 1, 0):
        return  # moved down OK
    lock_piece(state)
```

Flow each tick:

1. Try to move down one row.
2. If move succeeds, stop — piece is still falling.
3. If move fails, something blocked downward motion → lock.

That "fail to move down → lock" rule is the standard Tetris rule. It applies whether the block below is the floor, a wall of `#`, or another locked cell.

```python
# Simulate three gravity ticks on an open board
state = new_game_state()
start_row = state["piece_row"]
tick_gravity(state)
tick_gravity(state)
print(state["piece_row"])  # start_row + 2 if nothing blocked
```

## Hard Drop (Optional)

Some players want the piece to slam to the bottom instantly:

```python
def hard_drop(state):
    while try_move(state, 1, 0):
        pass
    lock_piece(state)
```

The `while` loop keeps dropping until `try_move` returns `False`, then locks once. Map to key `space` later in Pygame, or `h` in the text version.

Each `try_move` inside the loop still runs collision checks — the piece stops on the first obstacle, not inside it.

Add to `handle_input`:

```python
elif cmd == "h":
    hard_drop(state)
```

## Order of Operations Each Turn

A full turn ties input, gravity, and (soon) line clears together:

```python
def game_tick(state, cmd):
    if cmd:
        handle_input(state, cmd)
    if not state["game_over"]:
        tick_gravity(state)
        clear_full_lines(state)  # next chapter
```

Typical sequence when player presses `a` (left):

1. `handle_input` tries left move.
2. `tick_gravity` drops piece one row (or locks if blocked).
3. `clear_full_lines` removes any completed rows.

Adjust if you want gravity only on empty input — some text demos skip auto-fall when the player already pressed `s`. Either design is fine; stay consistent.

## Common Mistakes

| Mistake | What happens | Fix |
|---------|--------------|-----|
| Writing falling piece into `board` during draw | Ghost blocks, erasing stacks | Only `lock_piece` writes piece cells to `board` |
| Locking without spawn | No piece to control | Always call `spawn_new_piece` after lock |
| Locking when move sideways fails | Piece locks when hitting a wall | Only lock on **failed downward** move |
| Forgetting `row >= 0` | IndexError on negative row | Skip invisible cells when writing |

## Visual check after lock

After implementing lock, play one piece to the bottom and inspect the board:

```python
lock_piece(state)
for row in state["board"]:
    print("".join(row))
# expected: four new BLOCK cells where the piece landed; rest unchanged
```

Then confirm a new piece appears at the spawn position with different `name` or position.

## Try It Yourself

Play until piece lands. Print board — locked cells should stay after new piece spawns:

```python
while not state["game_over"]:
    draw_game(state)
    cmd = input("> ").strip().lower()
    if cmd == "":
        cmd = "s"  # fast test: keep soft dropping
    handle_input(state, cmd)
    tick_gravity(state)
```

Stack three or four pieces. Each lock should add permanent blocks while the active piece keeps moving independently.

## Summary

- **Lock** copies piece cells into `board` as permanent blocks.
- **Gravity** tries down first; failure triggers **lock**.
- **Spawn** new piece after every lock (unless game over).
- Hard drop repeats down moves then locks once.
- Next: **clear full lines**.

**Next:** [Clearing Full Lines](04-clearing-lines.md)
