---
title: Text and Strings
order: 3
---

# Chapter 10: Text and Strings

**Strings** are text — letters, digits, symbols in quotes. Tetris draws the board with strings like `"....##...."`.

## Creating Strings

```python
print("Hello")
print('Hello')   # single quotes work too
print("It's fine")  # double quotes when text has apostrophe
```

## String Length

```python
row = "....##...."
print(len(row))  # 10 characters
```

Board width = length of one row string.

## Concatenation — Gluing Strings

```python
greeting = "Hello" + " " + "World"
print(greeting)
```

Repeating:

```python
print("." * 10)  # ..........
print("#" * 4)   # ####
```

Empty cell = `"."`; filled cell = `"#"` in text Tetris.

## f-strings (Formatted Strings)

Embed values inside text (Python 3.6+):

```python
name = "Alex"
score = 1200
print(f"Player {name} scored {score}")
```

For Tetris:

```python
lines = 2
print(f"You cleared {lines} lines!")
```

## Indexing — One Character

Positions start at **0**:

```python
s = "Tetris"
print(s[0])  # T
print(s[1])  # e
print(s[-1]) # s (last)
```

## Slicing — Piece of a String

```python
row = "....##...."
print(row[4:6])  # ##
```

## Common String Methods

```python
text = "  hello  "
print(text.strip())      # "hello"
print(text.upper())      # "  HELLO  "
print("a,b,c".split(","))  # ['a', 'b', 'c']
```

## Escape Characters

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Quote inside string |

```python
print("Line1\nLine2")
```

## Strings Are Immutable

You cannot change one character in place:

```python
s = "cat"
# s[0] = "b"  # TypeError
s = "bat"     # OK — new string
```

## Try It Yourself

1. Build a 10-character row with 4 dots, 2 hashes, 4 dots (use `+` or `*`).
2. Use an f-string to print `Board size: 10 x 20`.
3. Print the third character of `"Tetromino"`.

## Summary

- **Strings** hold text in `"quotes"`.
- **`len`**, `+`, `*`**, **f-strings** are daily tools.
- Tetris board rows are strings of `.` and `#`.
- Next: ask the user for input.

**Next:** [Getting Input from the User](04-getting-input.html)
