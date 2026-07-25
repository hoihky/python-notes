---
title: Your First Program
order: 3
---

# Chapter 6: Your First Program

Time to run real Python code. We start with the classic **Hello, World!** — one line that proves everything is wired correctly.

## Create hello.py

In VS Code, inside `my_tetris`:

1. **New File** → save as `hello.py`
2. Type exactly:

```python
print("Hello, World!")
```

3. Save (`Ctrl+S` / `Cmd+S`).

## Run the Program

### Method 1 — Play button

Click the **▶ Run Python File** triangle (top right).

### Method 2 — Terminal

```bash
python3 hello.py
```

Windows:

```powershell
python hello.py
```

### Expected output

```
Hello, World!
```

If you see this, **Python works**. Celebrate — you are a programmer.

## What Each Part Means

```python
print("Hello, World!")
```

| Piece | Meaning |
|-------|---------|
| `print` | A **built-in function** — “show something on screen” |
| `(` `)` | Parentheses wrap what you give to `print` |
| `"Hello, World!"` | A **string** — text in quotes |

Python reads your file **top to bottom** and runs each line.

## Change It

Try:

```python
print("I am learning Python for Tetris!")
print(2026)
```

Run again. Two lines of output.

## When Something Goes Wrong — Errors

Example typo:

```python
prin("Hello")
```

Output might say:

```
NameError: name 'prin' is not defined
```

| Part of message | Meaning |
|-----------------|---------|
| `NameError` | Type of problem |
| `prin` is not defined | Python does not know `prin` — did you mean `print`? |

Read the **line number** in the error — click it in VS Code to jump there.

## Comments (Preview)

Lines starting with `#` are **comments** — notes for humans, ignored by Python:

```python
# My first program
print("Hello!")
```

## Try It Yourself

1. Make `hello.py` print your name.
2. Add a second `print` with your favorite food.
3. Introduce one typo on purpose — read the error, fix it.

## Summary

- Save code in **`.py`** files.
- **`print(...)`** shows text or numbers.
- Run with **terminal** or **Run** button.
- **Errors** name the problem and line — read them calmly.

**Next:** [Virtual Environments and pip](04-virtual-environments.html)
