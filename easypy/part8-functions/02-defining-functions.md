# Chapter 25: Defining and Calling Functions

Functions have two moments in their life: **definition** (writing the recipe) and **call** (cooking the meal). Python reads `def` blocks when the file loads, but the body runs only when something calls the name.

## Define a Function

```python
def say_hello():
    print("Hello from a function!")

say_hello()
say_hello()
# expected output (twice):
# Hello from a function!
# Hello from a function!
```

- `def` = define
- `say_hello` = name
- `()` = no parameters yet
- `:` then **indented body**

The body must be indented — usually four spaces. Python uses indentation to know what belongs inside the function.

## Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")
greet("Sam")
# expected output:
# Hello, Alex!
# Hello, Sam!
```

**Parameters** are placeholders in the definition; **arguments** are actual values you pass at the call site. `name` is the parameter; `"Alex"` is the argument.

## Multiple Parameters

```python
def show_position(col, row):
    print(f"Piece at ({col}, {row})")

show_position(4, 0)
# expected output: Piece at (4, 0)
```

Order matters: first argument fills first parameter. In Tetris you will often pass `board` first, then coordinates — pick an order and stay consistent across functions.

## return — Send Value Back

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

`return` hands a value back to whoever called the function. Without `return`, the function finishes and Python gives you `None` — "no useful value."

```python
def make_row(width):
    return ["."] * width

row = make_row(10)
print(len(row))  # 10
```

**Print vs return:** `print` shows text on screen. `return` passes data to the next line of **your** program. Tetris helpers usually **return** boards, booleans, or cell lists; only `draw_board` needs heavy `print` use.

## Docstrings (Good Habit)

```python
def make_board(width, height):
    """Create empty Tetris board as list of rows."""
    return [["."] * width for _ in range(height)]
```

Triple-quoted string right after `def` line — explains purpose. Future you (and teammates) see help when they forget what `make_board` does.

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

Save as `board.py`. Run it — you should see a blank 20-line grid of dots.

## Putting It Together — Call Chain

```python
def make_board():
    return [["."] * WIDTH for _ in range(HEIGHT)]

def place_dot(board, row, col):
    board[row][col] = "#"

def demo():
    b = make_board()
    place_dot(b, 0, 4)
    draw_board(b)

demo()
# expected: top row has one '#' near the middle
```

`demo()` calls three functions in order. The main loop in Tetris will look similar — orchestration on top, details inside helpers.

## Scope Preview

Variables inside function are **local**:

```python
def f():
    x = 10
    print("inside:", x)

f()
# print(x)  # NameError — x not visible outside
```

`x` exists only while `f()` runs. Board variables created in `make_board()` can be returned and used outside — the **list** travels; local temps do not.

## Common Mistakes

| Mistake | Result | Fix |
|---------|--------|-----|
| Forgetting `:` after `def name()` | SyntaxError | Always `def name():` |
| Wrong indent on body | Logic runs outside function | Indent body one level |
| Calling before `def` in same file | Usually OK if `def` runs first at load | Define functions above `main()` |
| Using `print` when you need `return` | Caller gets `None` | Return the list or boolean |

## Try It Yourself

Add `def set_cell(board, row, col, char):` that sets one cell and returns nothing.

Test it:

```python
b = make_board()
set_cell(b, 19, 0, "#")
set_cell(b, 19, 9, "#")
draw_board(b)
# expected: bottom row has '#' in corners
```

## Summary

- **`def name():`** defines; **`name()`** calls.
- **Parameters** pass data in; **`return`** sends data out.
- **`print`** for humans; **`return`** for the rest of your program.
- Start **`board.py`** with `make_board` and `draw_board`.

**Next:** [Parameters and Return Values](03-parameters-and-return.md)
