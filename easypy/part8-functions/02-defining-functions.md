---
title: Defining and Calling Functions
order: 2
---

# Chapter 25: Defining and Calling Functions

## Define a Function

```python
def say_hello():
    print("Hello from a function!")

say_hello()
say_hello()
```

- `def` = define
- `say_hello` = name
- `()` = no parameters yet
- `:` then **indented body**

## Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Sam")
```

**Parameters** are placeholders; **arguments** are actual values you pass.

## Multiple Parameters

```python
def show_position(col, row):
    print(f"Piece at ({col}, {row})")

show_position(4, 0)
```

## return — Send Value Back

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

Without `return`, function gives `None`.

```python
def make_row(width):
    return ["."] * width

row = make_row(10)
```

## Docstrings (Good Habit)

```python
def make_board(width, height):
    """Create empty Tetris board as list of rows."""
    return [["."] * width for _ in range(height)]
```

Triple-quoted string right after `def` line — explains purpose.

## Tetris Starter Functions

```python
WIDTH = 10
HEIGHT = 20

def make_board():
    return [["."] * WIDTH for _ in range(HEIGHT)]

def draw_board(board):
    print("\n" * 2)
    for row in board:
        print("".join(row))

board = make_board()
draw_board(board)
```

Save as `board.py`.

## Scope Preview

Variables inside function are **local**:

```python
def f():
    x = 10

f()
# print(x)  # NameError — x not visible outside
```

## Try It Yourself

Add `def set_cell(board, row, col, char):` that sets one cell and returns nothing.

## Summary

- **`def name():`** defines; **`name()`** calls.
- **Parameters** pass data in; **`return`** sends data out.
- Start **`board.py`** with `make_board` and `draw_board`.

**Next:** [Parameters and Return Values](03-parameters-and-return.html)
