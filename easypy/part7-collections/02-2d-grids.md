# Chapter 22: 2D Grids for Games

Tetris board is a **grid**: rows and columns. In Python: a **list of lists** — each inner list is one row.

Picture a spreadsheet or chess board. You need **two numbers** to point at one cell: which row (vertical) and which column (horizontal). Python stores the whole board as a list of rows; each row is itself a list of cell characters.

## Build Empty Board

```python
WIDTH = 10
HEIGHT = 20

def make_empty_board():
    board = []
    for _ in range(HEIGHT):
        row = ["."] * WIDTH
        board.append(row)
    return board

board = make_empty_board()
print(len(board))       # 20
print(len(board[0]))    # 10
```

The loop runs `HEIGHT` times. Each time it creates a **fresh** row list and appends it. That way row 0 and row 1 are separate lists — changing one does not change the other.

Or compact (common idiom):

```python
board = [["."] * WIDTH for _ in range(HEIGHT)]
```

This **list comprehension** does the same job in one line. You will see this pattern everywhere in game code.

## Read and Write a Cell

```python
row = 5
col = 3
board[row][col] = "#"

cell = board[row][col]
print(cell)  # #
```

**row** = vertical (y), **col** = horizontal (x).

Access is **two steps**: `board[row]` gets the whole row list, then `[col]` gets one character inside it. Say it aloud: "board, row five, column three."

## Draw Board

```python
def draw_board(board):
    print("\n" * 2)
    for row in board:
        print("".join(row))

draw_board(board)
```

Printing blank lines at the top pushes old output up so the grid is easier to see when you redraw many times in a loop.

Walkthrough of one draw:

1. Print two newlines (visual separation).
2. For each row in the board, join characters and print one line.
3. Result: a rectangle of dots — your empty Tetris well.

## Place a Small Shape

O-piece 2×2 at column 4, row 0:

```python
board[0][4] = "#"
board[0][5] = "#"
board[1][4] = "#"
board[1][5] = "#"
```

After this, the top-left area looks like a square of blocks. The falling piece is not "on the board" permanently yet in real Tetris — you draw it on top — but for practice, writing directly to `board` helps you learn coordinates.

## Coordinates Mental Model

```
col 0  1  2  3  4  5 ...
row 0  .  .  .  .  #  #
row 1  .  .  .  .  #  #
row 2  .  .  .  .  .  .
...
```

Row numbers **increase downward** — same as Tetris on screen. Column numbers increase to the right. Falling piece tracks `piece_row`, `piece_col` plus **shape offsets** (small `(dr, dc)` steps from the anchor).

## Why Not `[[ "."] * WIDTH] * HEIGHT`?

This looks tempting but breaks:

```python
# WRONG for a game board:
bad = [["."] * 3] * 3
bad[0][0] = "#"
print(bad)
# expected: only top-left changes
# actual: every row's first cell becomes '#'
```

All rows point at the **same** inner list. Always build each row separately — loop or comprehension.

## Copying Rows (Later)

When locking pieces, copy cell values — do not alias wrong lists.

```python
row = board[5]
new_row = row[:]  # shallow copy of one row
new_row[0] = "#"
print(board[5][0])  # still '.' — original row unchanged
```

`row[:]` means "copy all items from this row into a new list." When you merge a locked piece into the board, you often copy row slices or build fresh rows so old references do not surprise you.

## Count Blocks in a Row (Preview)

Full line clear checks whether a row has no empty cells:

```python
def count_blocks(row):
    count = 0
    for cell in row:
        if cell == "#":
            count += 1
    return count

bottom = board[-1]
print(count_blocks(bottom))  # 0 on empty board
```

You will use similar logic when asking "is this row completely full?"

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Swapping row and col | Piece appears sideways or out of bounds | Say "row first, then col": `board[row][col]` |
| Reusing one row list | Editing one row edits every row | New list per row in a loop |
| Drawing without `join` | `[ '.', '#', ...]` prints with brackets | `"".join(row)` for a clean line |
| Forgetting board height | IndexError on bottom row | Check `0 <= row < HEIGHT` before access |

## Try It Yourself

1. Create 10×6 empty board.
2. Draw a horizontal line of `#` on bottom row (loop over columns).
3. Draw board with `draw_board`.
4. **Bonus:** Place a 3-block vertical line in column 7 from row 2 down.

Save as `board.py` in `my_tetris`.

## Summary

- **2D board** = list of row lists.
- Access **`board[row][col]`**.
- Build rows with a **loop or comprehension**, never nested `*` alone.
- **`draw_board`** loops rows and joins characters.
- This is the **heart** of text Tetris.

**Next:** [Dictionaries](03-dictionaries.md)
