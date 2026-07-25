---
title: Editor and Development Tools
order: 2
---

# Chapter 5: Editor and Development Tools

You can write Python in Notepad, but a **code editor** colors your text, catches typos, and runs programs with one key. We recommend **Visual Studio Code** (free) or **Cursor** (also works great).

## Install Visual Studio Code

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download for your operating system.
3. Install with default options.

**Cursor** users: you already have a VS Code–compatible editor — follow the same extension steps below.

## Open Your Project Folder

1. Create folder `my_tetris` on your Desktop or Documents.
2. In VS Code: **File → Open Folder** → choose `my_tetris`.

You should see an empty file list on the left (**Explorer**).

## Install the Python Extension

1. Click the **Extensions** icon (square blocks) on the left.
2. Search **Python** (by Microsoft).
3. Click **Install**.

This adds:

- Syntax highlighting (colors for `print`, strings, etc.)
- **Run** button for Python files
- Debugger (later)

## Recommended Settings for Beginners

**File → Preferences → Settings**, search:

| Setting | Suggestion |
|---------|------------|
| Font size | 14–16 if text feels small |
| Word wrap | on (long lines wrap) |
| Auto Save | afterDelay |

## Integrated Terminal

**View → Terminal** (or `` Ctrl+` `` / `` Cmd+` ``).

You run Python here without leaving the editor:

```bash
python3 hello.py
```

Windows may use:

```powershell
python hello.py
```

## File Names

| Good | Bad |
|------|-----|
| `hello.py` | `hello.txt` (wrong extension) |
| `tetris_game.py` | `my game.py` (spaces awkward) |
| `board.py` | `Board.PY` (stick to lowercase `.py`) |

## Optional: Python from Command Palette

`Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) → type **Python: Select Interpreter** → pick Python 3.x.

## Try It Yourself

1. Open `my_tetris` in VS Code.
2. Install Python extension.
3. Open Terminal inside VS Code and run `python3 --version`.

## Summary

- Use **VS Code** (or Cursor) with the **Python extension**.
- Keep all Tetris files in **`my_tetris`**.
- Use the **integrated terminal** to run programs.
- Next: write and run `hello.py`.

**Next:** [Your First Program](03-first-program.html)
