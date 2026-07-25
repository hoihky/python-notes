---
title: Getting Input from the User
order: 4
---

# Chapter 11: Getting Input from the User

`print` sends information **out**. **`input`** brings information **in** — from the keyboard. Text Tetris will use keys like `a`, `d`, `s` for left, right, down.

## Basic input

```python
name = input("What is your name? ")
print("Hello,", name)
```

When Python hits `input`, it **waits** until the user presses **Enter**.

Whatever they typed (as text) is stored in `name`.

## input Always Returns a String

```python
age = input("How old are you? ")
print(type(age))  # <class 'str'>
```

Convert if you need a number:

```python
age = int(input("How old are you? "))
```

If they type `hello`, `int` fails — we handle that later.

## Simple Menu (Tetris Preview)

```python
print("Commands: a=left, d=right, s=down, q=quit")
command = input("Your move: ")
print("You pressed:", command)
```

Later one **game loop** reads command each turn.

## Empty Input

If user presses Enter without typing, you get `""` (empty string).

```python
text = input("Type something (or nothing): ")
if text == "":
    print("You entered nothing.")
```

## input Blocks the Program

The rest of your code **waits** during `input`. In graphical Tetris, Pygame reads keys differently (no Enter per move). Text Tetris uses `input` for simplicity while learning.

## Try It Yourself

Create `greet.py`:

1. Ask for name and favorite color.
2. Print a sentence using both with an f-string.
3. Ask for a number as string, convert with `int`, double it and print.

## Summary

- **`input(prompt)`** reads a line of text from the user.
- Result is always a **string** — use `int()` / `float()` if needed.
- Text Tetris commands start as simple **letter input**.
- Next: variables — storing values with names.

**Next:** [What Is a Variable?](../part4-variables/01-what-is-a-variable.html)
