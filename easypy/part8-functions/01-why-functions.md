# Chapter 24: Why Functions?

A **function** is a named recipe — a group of lines you run whenever you call the name. Without functions, Tetris becomes one endless file of copy-paste.

Imagine writing every recipe from scratch each time you cook pasta. You would copy the same steps onto sticky notes again and again. One typo on note #7 means dinner fails while notes #1–6 still look fine. Functions give you **one** sticky note labeled `make_pasta()` that you reuse.

## The Problem Without Functions

```python
board = [["."] * 10 for _ in range(20)]

# draw board — copy 1
for row in board:
    print("".join(row))

# ... 50 lines later ...

# draw board — copy 2 (oops, you fixed a bug in only one place)
for row in board:
    print("".join(row))  # forgot the blank lines at the top
```

The game loop might need to redraw after every move, after line clears, and after game over. Copy-paste three times and you will fix a bug in one copy but not the others.

## The Solution

```python
def draw_board(board):
    print("\n" * 2)
    for row in board:
        print("".join(row))

draw_board(board)
draw_board(board)  # same behavior, one definition
```

Now "how to draw" lives in **one place**. Change spacing or borders once — every call updates.

## Benefits

| Benefit | Tetris example |
|---------|----------------|
| **Reuse** | Draw after every move |
| **Readability** | `move_piece()` says what it does |
| **Easier fixes** | Change draw logic once |
| **Team work** | One person writes `clear_lines` |
| **Testing** | Run `make_board()` alone in a small script |

## Analogy

A function is like a **button** on a microwave:

- **Name** on button — `def heat_pizza()`
- **Instructions inside** — what happens when pressed
- **Press** — **call** the function

You do not rewire the microwave each lunch. You press the same button. Functions are your microwave buttons for code.

## Before and After — Mental Load

**Without functions**, reading Tetris code feels like:

> 200 lines of loops, prints, and `if` statements — where does drawing end and collision start?

**With functions**, the main loop might read:

```python
draw_board(board)
cmd = read_input()
try_move(board, piece, cmd)
```

Each line is a **chapter title**. You open the function when you need details.

## Built-in Functions You Know

- `print()`
- `len()`
- `input()`
- `range()`
- `int()`, `str()`

You will define your own. They work the same way: name, parentheses, sometimes arguments inside.

```python
print(len([1, 2, 3]))  # 3 — print calls len, len returns a number
```

## Tetris Functions We Will Write

| Function | Job |
|----------|-----|
| `make_board()` | Empty grid |
| `draw_board()` | Show grid |
| `can_move()` | Collision check |
| `lock_piece()` | Merge piece into board |
| `clear_lines()` | Remove full rows |
| `new_piece()` | Random shape |

None of these need to exist on day one. You can start with `make_board` and `draw_board`, then add others as the game grows. That is normal — functions let you grow in layers.

## When *Not* to Make a Function Yet

If you use a block of code **once** and it is only three lines, a function might wait. When you copy-paste it twice, or when the block has a clear name ("draw the score"), extract it.

Rule of thumb: **name things you want to think about as one step.**

## Common Mistakes

| Mistake | Why it hurts | Better approach |
|---------|--------------|-----------------|
| One giant `main()` with everything | Hard to find bugs | Split draw, input, move |
| Copy-paste instead of calling | Fixes miss a copy | One `draw_board` |
| Vague names like `do_stuff()` | You forget what it does | `clear_full_lines()` |
| Too many tiny one-line functions | Hard to navigate | Group related steps |

## Try It Yourself

Without looking ahead, list on paper 5 tasks Tetris does each turn. Each might become a function.

Example starter list: show board, read key, move piece, check collision, lock if landed. Circle which ones you already know how to write with lists and loops.

## Summary

- **Functions** group reusable steps.
- They make Tetris **maintainable** and easier to read.
- You already use built-in functions every day.
- Next: how to **define** and **call** them.

**Next:** [Defining and Calling Functions](02-defining-functions.md)
