# Chapter 6: Your First Program

Time to run real Python code. We start with the classic **Hello, World!** — one line that proves everything is wired correctly.

"Hello, World!" is a tradition, not a rule. Every programmer runs some tiny program first to confirm: editor saves files, terminal finds Python, output appears. Your Tetris journey starts here — one line at a time.

## Create hello.py

In VS Code, inside `my_tetris`:

1. **New File** → save as `hello.py`
2. Type exactly:

```python
print("Hello, World!")
```

3. Save (`Ctrl+S` / `Cmd+S`).

### Step-by-step: save and confirm

1. **File → New File** (or click the new file icon in Explorer).
2. Type the `print` line.
3. **File → Save As** → navigate to `my_tetris` → filename `hello.py`.
4. Check the tab title — it should say `hello.py`, not `Untitled`.
5. Look at Explorer: `hello.py` appears under your folder.

If the icon or tab shows a dot, the file has unsaved changes. Save before running.

## Run the Program

### Method 1 — Play button

Click the **▶ Run Python File** triangle (top right).

The first time, VS Code may ask which Python to use — pick Python 3.10+ from python.org or your system install.

### Method 2 — Terminal

```bash
python3 hello.py
# expected output: Hello, World!
```

Windows:

```powershell
python hello.py
# expected output: Hello, World!
```

Both methods run the **same** file. Use whichever you remember. Terminal skills matter later when you run `tetris.py` with arguments or activate a virtual environment.

### Expected output

```
Hello, World!
```

If you see this, **Python works**. Celebrate — you are a programmer.

If nothing appears, check that you saved the file and that the terminal's current folder is `my_tetris` (where `hello.py` lives).

## What Each Part Means

```python
print("Hello, World!")
```

| Piece | Meaning |
|-------|---------|
| `print` | A **built-in function** — "show something on screen" |
| `(` `)` | Parentheses wrap what you give to `print` |
| `"Hello, World!"` | A **string** — text in quotes |

Python reads your file **top to bottom** and runs each line.

Functions are reusable actions. `print` is built into Python — you do not define it yourself. Later you will define your own functions like `draw_board()` for Tetris.

## Change It

Try:

```python
print("I am learning Python for Tetris!")
print(2026)
# expected output:
# I am learning Python for Tetris!
# 2026
```

Run again. Two lines of output.

`print` accepts text in quotes **or** numbers without quotes. Tetris will use both: strings for the grid, numbers for score and positions.

### More experiments

```python
print("Line 1")
print("Line 2")
print(10 + 5)
# expected output:
# Line 1
# Line 2
# 15
```

Each `print` runs in order. The third line computes math before displaying `15`.

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

Errors feel harsh at first. Treat them as **labeled problems**: the type (`NameError`, `SyntaxError`) narrows the search; the line number points to where Python got confused — not always the true bug, but always the right place to start looking.

### Another common error: missing quote

```python
print("Hello)
# SyntaxError: unterminated string literal
```

Python started a string at `"` but never found the closing quote. Fix the quotes, save, run again.

## Comments (Preview)

Lines starting with `#` are **comments** — notes for humans, ignored by Python:

```python
# My first program
print("Hello!")
# expected output: Hello!
```

We cover comments fully in the next part. For now, use them to label sections in `hello.py`.

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Wrong file extension | Python does not run or runs wrong file | Save as `.py` |
| Forgot to save | Old output after edits | Save before Run |
| Wrong folder in terminal | `No such file or directory` | `cd` to `my_tetris` |
| Smart quotes `"Hello"` | `SyntaxError` | Use straight `"` quotes on keyboard |

## Try It Yourself

1. Make `hello.py` print your name.
2. Add a second `print` with your favorite food.
3. Introduce one typo on purpose — read the error, fix it.

Optional Tetris teaser: add `print("Soon: falling blocks!")` as a third line — a reminder of where this tutorial goes.

## Summary

- Save code in **`.py`** files.
- **`print(...)`** shows text or numbers.
- Run with **terminal** or **Run** button.
- **Errors** name the problem and line — read them calmly.

**Next:** [Virtual Environments and pip](04-virtual-environments.md)
