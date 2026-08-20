# Chapter 5: Editor and Development Tools

You can write Python in Notepad, but a **code editor** colors your text, catches typos, and runs programs with one key. We recommend **Visual Studio Code** (free) or **Cursor** (also works great).

A good editor does not write code for you — it makes code **easier to read and fix**. Syntax colors help you spot an unclosed quote; the integrated terminal keeps run commands in one place. For Tetris, you will jump between several files; the Explorer sidebar keeps them organized.

## Install Visual Studio Code

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download for your operating system.
3. Install with default options.

**Cursor** users: you already have a VS Code–compatible editor — follow the same extension steps below.

During install, optional checkboxes like "Add to PATH" or "Open with Code" are fine to accept. They are not required for this tutorial but can save clicks later.

## Open Your Project Folder

1. Create folder `my_tetris` on your Desktop or Documents.
2. In VS Code: **File → Open Folder** → choose `my_tetris`.

You should see an empty file list on the left (**Explorer**).

Opening the **folder**, not just a single file, matters. When Tetris grows to `board.py`, `shapes.py`, and `tetris.py`, you want all of them visible in one workspace.

### Step-by-step: confirm the workspace

1. **File → Open Folder** → select `my_tetris`.
2. In Explorer, right-click → **New File** → type `notes.txt` → Enter.
3. Save with `Ctrl+S` / `Cmd+S`.
4. The file name appears under `my_tetris` — you are in the right place.

## Install the Python Extension

1. Click the **Extensions** icon (square blocks) on the left.
2. Search **Python** (by Microsoft).
3. Click **Install**.

This adds:

- Syntax highlighting (colors for `print`, strings, etc.)
- **Run** button for Python files
- Debugger (later)

After install, open any `.py` file — keywords like `print` should appear in color. If everything is plain black text, click the language mode in the bottom-right corner and choose **Python**.

## Recommended Settings for Beginners

**File → Preferences → Settings**, search:

| Setting | Suggestion |
|---------|------------|
| Font size | 14–16 if text feels small |
| Word wrap | on (long lines wrap) |
| Auto Save | afterDelay |

**Word wrap** prevents long `print` lines from scrolling off-screen. **Auto Save** reduces "I forgot to save before running" moments — a classic beginner surprise when output does not match what you just typed.

## Integrated Terminal

**View → Terminal** (or `` Ctrl+` `` / `` Cmd+` ``).

You run Python here without leaving the editor:

```bash
python3 hello.py
# expected output depends on hello.py contents
```

Windows may use:

```powershell
python hello.py
```

The terminal opens **inside** your project folder when you opened the folder correctly. If `hello.py` is "not found," run `cd` to your `my_tetris` path first, or use **Terminal → New Terminal** after opening the folder.

### Terminal vs external window

Both work. The integrated terminal is convenient because you can edit on the left and run on the bottom without alt-tabbing. Use the same Python command you verified in Chapter 4 (`python3` or `python`).

## File Names

| Good | Bad |
|------|-----|
| `hello.py` | `hello.txt` (wrong extension) |
| `tetris_game.py` | `my game.py` (spaces awkward) |
| `board.py` | `Board.PY` (stick to lowercase `.py`) |

On some systems, `Board.PY` and `board.py` are treated as different files. Stick to **lowercase** names with underscores — a habit that avoids confusion when Tetris imports grow more complex.

## Optional: Python from Command Palette

`Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) → type **Python: Select Interpreter** → pick Python 3.x.

Do this after you create a virtual environment (next chapter) so VS Code runs code with the correct Python and packages. For now, picking any Python 3.10+ interpreter is enough.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Editing a file outside `my_tetris` | **File → Open Folder** on `my_tetris` |
| Running `.py` from wrong directory | `cd` to folder containing the file |
| No colors in editor | Install Python extension; set language to Python |
| Saving as `hello.py.txt` | Turn off "hide extensions" in OS settings; save as `hello.py` |

## Try It Yourself

1. Open `my_tetris` in VS Code.
2. Install Python extension.
3. Open Terminal inside VS Code and run `python3 --version`.

Bonus: create `notes.txt` in the Explorer and list your Python version and editor name. You will thank yourself when switching computers later.

## Summary

- Use **VS Code** (or Cursor) with the **Python extension**.
- Keep all Tetris files in **`my_tetris`**.
- Use the **integrated terminal** to run programs.
- Next: write and run `hello.py`.

**Next:** [Your First Program](03-first-program.md)
