# Chapter 10: Text and Strings

**Strings** are text — letters, digits, symbols in quotes. Tetris draws the board with strings like `"....##...."`.

Each row of the text board **is** one string. Empty cells are dots; filled cells are hashes. No special graphics — just characters arranged in order. That simplicity lets you focus on game logic first.

## Creating Strings

```python
print("Hello")
print('Hello')   # single quotes work too
print("It's fine")  # double quotes when text has apostrophe
# expected output (three lines):
# Hello
# Hello
# It's fine
```

Pick single or double quotes and stay consistent within a project. This tutorial prefers double quotes for board rows so apostrophes in messages stay easy.

## String Length

```python
row = "....##...."
print(len(row))  # expected output: 10
```

Board width = length of one row string.

Before drawing Tetris, you can assert `len(row) == 10` mentally — or with code later. Wrong-length rows are the #1 cause of "slanted" text boards.

## Concatenation — Gluing Strings

```python
greeting = "Hello" + " " + "World"
print(greeting)
# expected output: Hello World
```

Repeating:

```python
print("." * 10)  # expected output: ..........
print("#" * 4)   # expected output: ####
```

Empty cell = `"."`; filled cell = `"#"` in text Tetris.

Multiplication on strings repeats them — a shortcut for empty rows:

```python
empty_row = "." * 10
print(empty_row)
# expected output: ..........
```

### Building a row piece by piece

```python
left = "." * 4
middle = "##"
right = "." * 4
row = left + middle + right
print(row)
print(len(row))
# expected output:
# ....##....
# 10
```

Same visual as typing `"....##...."` — but shows how rows assemble from parts when pieces move.

## f-strings (Formatted Strings)

Embed values inside text (Python 3.6+):

```python
name = "Alex"
score = 1200
print(f"Player {name} scored {score}")
# expected output: Player Alex scored 1200
```

For Tetris:

```python
lines = 2
print(f"You cleared {lines} lines!")
# expected output: You cleared 2 lines!
```

Put an `f` before the opening quote. Curly braces `{variable}` mark where values plug in — cleaner than `"Score: " + str(score)` for longer messages.

### f-string with expressions

```python
width = 10
height = 20
print(f"Board size: {width} x {height}")
# expected output: Board size: 10 x 20
```

You can put simple expressions inside braces: `{width * height}` for cell count, for example.

## Indexing — One Character

Positions start at **0**:

```python
s = "Tetris"
print(s[0])  # expected output: T
print(s[1])  # expected output: e
print(s[-1]) # expected output: s (last)
```

Negative indices count from the end: `-1` is last character, `-2` is second-to-last. Handy for checking the rightmost cell in a row string.

## Slicing — Piece of a String

```python
row = "....##...."
print(row[4:6])  # expected output: ##
```

Slice `[start:end]` takes characters from `start` up to **but not including** `end`. Here columns 4 and 5 are the two `#` symbols.

### Reading one cell

```python
row = "....##...."
column = 4
cell = row[column]
print(cell)
# expected output: #
```

Later, a 2D list replaces one long string per row — but the idea "each column has an address" stays the same.

## Common String Methods

```python
text = "  hello  "
print(text.strip())      # expected output: hello
print(text.upper())      # expected output:   HELLO  
print("a,b,c".split(","))  # expected output: ['a', 'b', 'c']
```

Methods are actions attached to values: `text.strip()` trims whitespace; `"a,b,c".split(",")` cuts a string into a list. You will use `split` more when reading config files — less in core Tetris logic.

## Escape Characters

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Quote inside string |

```python
print("Line1\nLine2")
# expected output:
# Line1
# Line2
```

Escape sequences start with backslash `\`. They let you put special characters inside strings without ending the string early.

## Strings Are Immutable

You cannot change one character in place:

```python
s = "cat"
# s[0] = "b"  # TypeError: 'str' object does not support item assignment
s = "bat"     # OK — new string
print(s)
# expected output: bat
```

Immutability means every "change" builds a **new** string. Tetris row updates will create new row strings or switch to lists — both patterns appear later.

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Mixing quote types unclosed | `SyntaxError` | Match opening and closing quote |
| Off-by-one slice | Wrong cell extracted | Remember end index is excluded |
| `"5" + 5` | `TypeError` | `"5" + str(5)` or convert first |
| Smart quotes `"text"` | `SyntaxError` | Straight keyboard quotes |

## Try It Yourself

1. Build a 10-character row with 4 dots, 2 hashes, 4 dots (use `+` or `*`).
2. Use an f-string to print `Board size: 10 x 20`.
3. Print the third character of `"Tetromino"`.

Hints:

```python
# 1
row = "." * 4 + "##" + "." * 4

# 3 — index 2 is the third character (0-based)
print("Tetromino"[2])  # expected output: t
```

Save as `strings_demo.py`, run it, and compare output to what you expect.

## Summary

- **Strings** hold text in `"quotes"`.
- **`len`**, `+`, `*`, **f-strings** are daily tools.
- Tetris board rows are strings of `.` and `#`.
- Next: ask the user for input.

**Next:** [Getting Input from the User](04-getting-input.md)
