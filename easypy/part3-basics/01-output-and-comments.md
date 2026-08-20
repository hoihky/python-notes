# Chapter 8: Output and Comments

Programs that never show anything feel broken. **`print`** is how your program **talks to you** — essential for learning and for drawing our text Tetris board.

In text Tetris, the "screen" **is** the terminal output. Every frame, your game will `print` row after row until the whole grid appears. Mastering `print` now saves frustration when the board looks crooked later.

## print in Detail

```python
print("Hello")
print(100)
print(3.14)
# expected output:
# Hello
# 100
# 3.14
```

Each call usually prints on its **own line**.

You can pass almost any value to `print` — text, whole numbers, decimals. Tetris will print strings for the grid and numbers for score on separate lines or the same line depending on formatting.

### Multiple items

```python
print("Score:", 1200)
# expected output: Score: 1200
```

Output: `Score: 1200` (space between items by default).

This form is handy for debug messages: `print("piece_x is", piece_x)` without building a full sentence first.

### sep and end (Optional)

```python
print("A", "B", "C", sep="-")
# expected output: A-B-C

print("Loading", end="...")
print(" done!")
# expected output: Loading... done!
```

By default, `sep` is a space and `end` is a newline (`\n`). Changing them lets you build custom layouts — useful when printing a row of cells without automatic line breaks between each character (advanced Tetris formatting).

## Comments — Notes for Humans

```python
# This line is ignored by Python
print("Visible")  # comment after code also works
# expected output: Visible
```

Use comments to explain **why**, not what obvious code does:

```python
# Good
# Wait until player presses Enter before next turn
input("Press Enter...")

# Less helpful
print("hi")  # prints hi
```

Comments never run — they are for you and teammates. When you return to Tetris code after a break, a short comment like `# check left collision` saves re-reading twenty lines.

### Multi-line comments

Python has no special `/* */` block. Use multiple `#` lines or triple-quoted strings (usually for text data, not ideal for comments).

Preferred style for a short block:

```python
# Draw the board from top row to bottom.
# Each row is a string of dots and hashes.
# Width must stay 10 characters.
```

Triple-quoted strings ** sitting alone** can act like comments but are easy to misuse — stick with `#` while learning.

## Debugging with print

When Tetris acts weird, beginners **print variables**:

```python
x = 5
print("x is", x)
# expected output: x is 5
```

You will use this constantly until you learn a debugger.

If a piece vanishes or lands in the wrong column, print `piece_x` and `piece_y` inside the game loop. Compare what you **expect** with what Python **shows**. Nine times out of ten, the bug is in the numbers, not in `print` itself.

### A mini walkthrough: finding an off-by-one bug

```python
width = 10
position = 10
print("position:", position, "width:", width)
print("Last valid column is", width - 1)
# expected output:
# position: 10 width: 10
# Last valid column is 9
```

Columns `0` through `9` fit on a width-10 board — not `10`. Printing makes that visible before you embed the logic in Tetris.

## Empty print

```python
print()
# expected output: (blank line)
```

Prints a blank line — useful spacing when showing the board.

A quick sequence:

```python
print("=== Tetris ===")
print()
print("....##....")
# expected output:
# === Tetris ===
#
# ....##....
```

Separates the title from the grid the way a blank line separates paragraphs in text.

## Tetris Preview — A Single Row

```python
print("..........")  # 10 dots = empty row (10 columns wide)
print("....##....")  # two blocks in the middle
# expected output:
# ..........
# ....##....
```

Our board is **text art** built from `print` inside loops (later).

Count the characters in each row — **10** for a standard Tetris well width. If a row shows 9 or 11 characters, the board will look jagged when stacked.

## Common Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Forgetting quotes around text | `NameError` or odd output | Use `print("text")` |
| Printing without running saved file | Old output | Save, then run again |
| Commenting with `//` like other languages | `SyntaxError` | Use `#` only |
| Too many debug prints at once | Hard to read output | Print one variable at a time |

## Try It Yourself

Create `output_demo.py`:

1. Print your name, age, and city on three lines.
2. Print one line with three words separated by `|`.
3. Add comments explaining each section.

Example structure (write your own values):

```python
# --- About me ---
print("Alex")
print(25)
print("Tokyo")

# --- Custom separator ---
print("Tetris", "Python", "Fun", sep="|")
# expected output: Tetris|Python|Fun
```

Run with `python3 output_demo.py` and confirm output matches what you intended.

## Summary

- **`print`** displays values; multiple arguments allowed.
- **`#`** comments document your thinking.
- Use **print to debug** — see what variables hold.
- Tetris rows start as strings of `.` and `#`.

**Next:** [Numbers and Math](02-numbers-and-math.md)
