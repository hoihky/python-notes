---
title: Output and Comments
order: 1
---

# Chapter 8: Output and Comments

Programs that never show anything feel broken. **`print`** is how your program **talks to you** — essential for learning and for drawing our text Tetris board.

## print in Detail

```python
print("Hello")
print(100)
print(3.14)
```

Each call usually prints on its **own line**.

### Multiple items

```python
print("Score:", 1200)
```

Output: `Score: 1200` (space between items by default).

### sep and end (Optional)

```python
print("A", "B", "C", sep="-")
# A-B-C

print("Loading", end="...")
print(" done!")
# Loading... done!
```

## Comments — Notes for Humans

```python
# This line is ignored by Python
print("Visible")  # comment after code also works
```

Use comments to explain **why**, not what obvious code does:

```python
# Good
# Wait until player presses Enter before next turn
input("Press Enter...")

# Less helpful
print("hi")  # prints hi
```

### Multi-line comments

Python has no special `/* */` block. Use multiple `#` lines or triple-quoted strings (usually for text data, not ideal for comments).

## Debugging with print

When Tetris acts weird, beginners **print variables**:

```python
x = 5
print("x is", x)
```

You will use this constantly until you learn a debugger.

## Empty print

```python
print()
```

Prints a blank line — useful spacing when showing the board.

## Tetris Preview — A Single Row

```python
print("..........")  # 10 dots = empty row (10 columns wide)
print("....##....")  # two blocks in the middle
```

Our board is **text art** built from `print` inside loops (later).

## Try It Yourself

Create `output_demo.py`:

1. Print your name, age, and city on three lines.
2. Print one line with three words separated by `|`.
3. Add comments explaining each section.

## Summary

- **`print`** displays values; multiple arguments allowed.
- **`#`** comments document your thinking.
- Use **print to debug** — see what variables hold.
- Tetris rows start as strings of `.` and `#`.

**Next:** [Numbers and Math](02-numbers-and-math.html)
