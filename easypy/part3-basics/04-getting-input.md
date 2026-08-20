# Chapter 11: Getting Input from the User

`print` sends information **out**. **`input`** brings information **in** — from the keyboard. Text Tetris will use keys like `a`, `d`, `s` for left, right, down.

Think of `input` as a **pause button**: your program stops, shows a prompt, and waits for the player. That turn-based style is simpler than real-time graphics while you learn collision and grid logic.

## Basic input

```python
name = input("What is your name? ")
print("Hello,", name)
# example session:
# What is your name? Sam
# Hello, Sam
```

When Python hits `input`, it **waits** until the user presses **Enter**.

Whatever they typed (as text) is stored in `name`.

The prompt string is optional but helpful — it tells the user what you expect. Tetris will use short prompts like `"Move (a/d/s/q): "`.

### Step-by-step: what happens at runtime

1. Python prints the prompt (no newline before you type — cursor stays on same line).
2. User types characters; Python collects them.
3. User presses Enter.
4. Python returns everything typed **before** Enter as a string.
5. The next line (`print("Hello,", name)`) runs.

## input Always Returns a String

```python
age = input("How old are you? ")
print(type(age))  # expected output: <class 'str'>
```

Even if the user types `25`, Python stores `"25"` — text, not a number. Math like `age + 1` fails until you convert.

Convert if you need a number:

```python
age = int(input("How old are you? "))
print(age + 1)
# example session if user types 25:
# How old are you? 25
# 26
```

If they type `hello`, `int` fails — we handle that later.

### Safe pattern preview (convert carefully)

```python
text = input("Enter a number: ")
if text.isdigit():
    number = int(text)
    print("Double:", number * 2)
else:
    print("That was not a whole number.")
# example if user types 7:
# Double: 14
```

Full error handling comes in a later chapter; this shows why "always a string" matters for Tetris menus and scores.

## Simple Menu (Tetris Preview)

```python
print("Commands: a=left, d=right, s=down, q=quit")
command = input("Your move: ")
print("You pressed:", command)
# example session:
# Commands: a=left, d=right, s=down, q=quit
# Your move: d
# You pressed: d
```

Later one **game loop** reads command each turn.

Each loop iteration: draw board → ask for move → update piece → repeat. Real Tetris feels continuous; text Tetris feels like chess — one move per prompt. Same rules, different pacing.

### Chaining commands in one session

```python
print("Mini Tetris controls: a/d/s/q")
move1 = input("Move 1: ")
move2 = input("Move 2: ")
print(f"You chose {move1} then {move2}")
```

Two prompts means two turns. A `while` loop (later) replaces duplicated lines with "keep asking until quit."

## Empty Input

If user presses Enter without typing, you get `""` (empty string).

```python
text = input("Type something (or nothing): ")
if text == "":
    print("You entered nothing.")
else:
    print("You typed:", text)
```

Empty input is still valid input — distinguish it from "user pressed q to quit" by checking `text == ""` or `text == "q"` separately.

## input Blocks the Program

The rest of your code **waits** during `input`. In graphical Tetris, Pygame reads keys differently (no Enter per move). Text Tetris uses `input` for simplicity while learning.

While blocked, the game cannot animate falling pieces on its own — gravity will be simulated **one row per turn** in early versions. That is a feature for learning: you see each state before the next move.

### print + input together

```python
print("=== Text Tetris (demo) ===")
print("Score: 0")
command = input("Move (a/d/s/q): ")
print(f"OK, processing: {command}")
# expected flow: banner, score line, prompt, confirmation
```

Pattern you will reuse: show state, ask for action, confirm or update.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| `age = input()` then `age + 1` | `TypeError` | `int(input(...))` when appropriate |
| Expecting single key without Enter | User must press Enter | Normal for `input`; Pygame differs later |
| Case-sensitive commands | `A` not same as `a` | Use `.lower()` on command string later |
| Spaces in input | `" d"` is not `"d"` | `.strip()` removes extra spaces |

Example with strip:

```python
command = input("Move: ").strip().lower()
print(repr(command))
# user types "  D  " + Enter → expected output: 'd'
```

## Try It Yourself

Create `greet.py`:

1. Ask for name and favorite color.
2. Print a sentence using both with an f-string.
3. Ask for a number as string, convert with `int`, double it and print.

Skeleton to fill in (use your own prompts):

```python
name = input("Name: ")
color = input("Favorite color: ")
print(f"Hi {name}, I bet {color} would look great on a Tetris piece.")

num_text = input("Pick a number: ")
num = int(num_text)
print(f"Double is {num * 2}")
```

Run it twice — once with a valid number, once with text — and notice when `int` crashes. That crash is the same kind you will guard against in score entry later.

## Summary

- **`input(prompt)`** reads a line of text from the user.
- Result is always a **string** — use `int()` / `float()` if needed.
- Text Tetris commands start as simple **letter input**.
- Next: variables — storing values with names.

**Next:** [What Is a Variable?](../part4-variables/01-what-is-a-variable.md)
