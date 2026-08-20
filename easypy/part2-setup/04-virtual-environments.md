# Chapter 7: Virtual Environments and pip

Later we install **Pygame** for graphics. First, learn **pip** (install extra packages) and **virtual environments** (keep each project's packages separate).

Think of a virtual environment as a **private toolbox** for one project — so Tetris libraries do not mix with other homework.

Without a venv, `pip install pygame` puts Pygame in a shared global folder. Another Python project might need a different version of the same library — conflicts follow. A venv gives each project its own shelf in the toolbox.

## What Is pip?

**pip** is Python's **package installer**. It downloads code other people wrote (libraries) from the internet.

Check pip:

```bash
python3 -m pip --version
# expected output example: pip 24.0 from ... (python 3.12)
```

Windows:

```powershell
python -m pip --version
# expected output example: pip 24.0 from ... (python 3.12)
```

Using `python3 -m pip` (or `python -m pip`) guarantees pip matches **that** Python interpreter — safer than a stray `pip` command that might point elsewhere.

## Install a Package (Example)

We will use Pygame in Part 12. Preview:

```bash
python3 -m pip install pygame
# downloads and installs pygame into the active environment
```

For now, you do **not** need to install it yet.

When you do install later, you will see download progress in the terminal. Success usually ends with `Successfully installed pygame-x.y.z`.

## Create a Virtual Environment

In terminal, go to your project:

```bash
cd ~/Desktop/my_tetris
# or your actual path
```

Create the environment (folder `venv`):

```bash
python3 -m venv venv
# creates a venv folder (no output on success is normal)
```

Windows:

```powershell
python -m venv venv
```

A folder **`venv`** appears — do not edit files inside manually.

The `venv` folder holds a copy of Python plus a place for installed packages. It can be large; that is normal. Add `venv/` to `.gitignore` if you use Git later — you recreate it from `requirements.txt`, not by copying the folder.

### Step-by-step: create venv from scratch

1. Open integrated terminal in VS Code with `my_tetris` open.
2. Run `python3 -m venv venv` (or `python -m venv venv` on Windows).
3. Wait a few seconds — Explorer may show a new `venv` folder.
4. Proceed to activation below before installing anything.

## Activate the Environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

When active, your prompt often shows `(venv)`:

```
(venv) user@computer:~/my_tetris$
```

Now `pip install` affects **only** this project.

Activation lasts for **that terminal window**. Open a new terminal → activate again. Forgetting to activate and then running `pip install` is a common mistake — packages go global instead of into `my_tetris`.

### PowerShell execution policy (Windows)

If PowerShell blocks activation with a security error, run once (as allowed on your machine):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then retry `.\venv\Scripts\Activate.ps1`. Command Prompt's `activate.bat` avoids this issue if you prefer.

## Deactivate

```bash
deactivate
# prompt returns to normal; (venv) disappears
```

Deactivating does not delete anything — it just stops routing `pip` and `python` through the venv for that terminal session.

## requirements.txt (Good Habit)

List packages your project needs:

```
pygame>=2.5.0
```

Install everything listed:

```bash
pip install -r requirements.txt
# reads the file and installs each package listed
```

We will add this when we reach Pygame.

On a new computer, you recreate the project with: create venv → activate → `pip install -r requirements.txt`. No guessing which libraries you needed six months ago.

## VS Code and venv

After creating `venv`, select interpreter:

**Python: Select Interpreter** → choose `./venv/bin/python` (path varies).

On Windows the path looks like `./venv/Scripts/python.exe`. VS Code then runs and debugs using packages from **your** venv, not the system Python.

## Common Mistakes

| Mistake | What went wrong | Fix |
|---------|-----------------|-----|
| `pip install` without activating | Package installed globally | Activate `(venv)` first |
| Editing files inside `venv/` | Breaks the environment | Delete `venv` and recreate |
| Committing `venv/` to Git | Huge, machine-specific folder | Ignore it; use `requirements.txt` |
| Wrong Python in VS Code | Imports fail after install | **Select Interpreter** → venv |

## Try It Yourself

1. Create `venv` inside `my_tetris`.
2. Activate it.
3. Run `pip list` — see installed packages (short list at first).
4. Deactivate.

Optional: with venv active, run `which python3` (Mac/Linux) or `where python` (Windows) — the path should point **inside** your `venv` folder. That confirms activation worked.

## Summary

- **pip** installs third-party packages.
- **venv** isolates packages per project.
- **Activate** venv before `pip install` for Tetris.
- Next: learn `print` and comments in depth.

**Next:** [Output and Comments](../part3-basics/01-output-and-comments.md)
