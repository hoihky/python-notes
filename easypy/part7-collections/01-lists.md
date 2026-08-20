# Chapter 21: Lists — Storing Many Values

A **list** holds many values in **order** — like a shopping list or one **row** of the Tetris board.

Think of a list as a row of numbered lockers. Each locker has a number (the **index**) starting at 0, and you can peek inside, swap what is stored, or add a new locker at the end. In Tetris, one horizontal row of the playfield is exactly one list of characters: mostly empty `.` cells, sometimes filled `#` blocks.

## Create a List

```python
empty_row = [".", ".", ".", ".", "."]
scores = [100, 200, 150]
mixed = [1, "hello", True]  # allowed but avoid mixing in Tetris
```

Square brackets `[ ]` mean "this is a list." Items are separated by commas. For Tetris, keep each list to one type — usually strings like `"."` and `"#"` — so your board stays easy to read and debug.

You can also build a list from nothing and fill it later:

```python
board_row = []
board_row.append(".")
board_row.append(".")
print(board_row)  # ['.', '.']
```

## Access by Index

```python
row = [".", ".", "#", "#", "."]
print(row[0])   # .
print(row[2])   # #
print(row[-1])  # .
```

**Index 0** is the first item, not the first "human" number. That trips up many beginners — if you want the third cell, use index `2`.

Negative indices count from the end: `row[-1]` is the last cell, `row[-2]` is second from the end. Handy when you care about the bottom of a row without knowing the exact width.

## Change an Item

```python
row = [".", ".", ".", ".", "."]
row[2] = "#"
print(row)  # ['.', '.', '#', '.', '.']
```

Lists are **mutable** — you can change cells in place. Strings are different: you cannot do `"hello"[0] = "H"` without creating a new string. Lists let you update one slot and keep the rest.

## Length

```python
row = [".", ".", "#", "#", "."]
print(len(row))  # 5
```

`len()` tells you how many items are in the list. For a Tetris row, `len(row)` should always match `WIDTH` (usually 10). If it does not, something went wrong when you built the board.

## Append and Pop

```python
history = []
history.append("I-piece")
history.append("O-piece")
history.append("T-piece")
print(history)  # ['I-piece', 'O-piece', 'T-piece']

last = history.pop()
print(last)     # T-piece
print(history)  # ['I-piece', 'O-piece']
```

- **`append(x)`** adds one item to the **end**.
- **`pop()`** removes and returns the **last** item.

You might use a list like `history` to remember which pieces appeared recently. `pop()` is also useful when you want "take the top item off a stack" — last in, first out.

## Loop Over a List

```python
row = [".", "#", "#", ".", "."]
for cell in row:
    print(cell, end="")
print()
# expected output: ..##.
```

The loop visits each item **in order**. Using `end=""` keeps characters on one line instead of printing each on its own line.

You can also loop by index when you need the position:

```python
row = [".", "#", ".", "#", "."]
for i in range(len(row)):
    if row[i] == "#":
        print(f"Block at column {i}")
# expected output:
# Block at column 1
# Block at column 3
```

That pattern — "for each index, check the cell" — shows up again when clearing full lines in Tetris.

## List from range

```python
zeros = [0] * 10
print(zeros)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

WIDTH = 10
row = ["."] * WIDTH
print(len(row))  # 10
```

Multiplying a list by a number repeats the **same reference** for each slot. For a flat row of dots, that is fine — every cell should be `"."`.

**Caution:** `[["."] * WIDTH] * HEIGHT` duplicates the **same inner list** — changing one row changes all rows. Use the 2D chapter for a proper board.

## Slicing — A Piece of a List

A **slice** grabs a sub-range without changing the original:

```python
row = [".", ".", "#", "#", ".", ".", ".", ".", ".", "."]
middle = row[2:4]
print(middle)  # ['#', '#']
print("".join(middle))  # ##
```

Syntax: `list[start:end]` — includes `start`, stops **before** `end`. Slicing is useful when you want to inspect part of a row, not the whole thing.

## Common Mistakes

| Mistake | What goes wrong | Fix |
|---------|-----------------|-----|
| Using index `10` on a width-10 row | `IndexError` — valid indices are 0–9 | Use `len(row) - 1` for the last index |
| Forgetting lists start at 0 | Off-by-one placement of blocks | Draw a numbered sketch: 0, 1, 2 … |
| `row = "." * WIDTH` | Creates a **string**, not a list | Use `[ "."] * WIDTH` with square brackets |
| Aliasing with `*` on nested lists | All rows share one list | Build rows in a loop or list comprehension |

## Tetris — One Row

```python
WIDTH = 10
row = ["."] * WIDTH
row[4] = "#"
row[5] = "#"
print("".join(row))  # ....##....
```

`"".join(row)` glues characters into one string for printing. The empty string `""` means "no separator between items" — perfect for a text grid.

Step by step:

1. Make 10 empty cells.
2. Set columns 4 and 5 to blocks (two adjacent `#`).
3. Join and print — you see a mini slice of a Tetris row.

When you stack many such rows, you get a full board — that is the next chapter.

## Try It Yourself

1. Make list of 10 dots, set indices 3 and 4 to `#`, print with `join`.
2. Append three shape names to a list; loop and print each.
3. **Bonus:** Use a loop to count how many `#` are in a row (preview of line-clear logic).

## Summary

- **Lists** `[ ]` store ordered items.
- **Index** from 0; **mutable** assignment.
- One board **row** = list of characters.
- **`append`**, **`pop`**, **`len`**, and **`join`** are everyday tools.
- Next: **2D grid** = list of lists.

**Next:** [2D Grids for Games](02-2d-grids.md)
