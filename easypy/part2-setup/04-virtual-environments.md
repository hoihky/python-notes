---
title: Virtual Environments and pip
order: 4
---

# Chapter 7: Virtual Environments and pip

Later we install **Pygame** for graphics. First, learn **pip** (install extra packages) and **virtual environments** (keep each project’s packages separate).

Think of a virtual environment as a **private toolbox** for one project — so Tetris libraries do not mix with other homework.

## What Is pip?

**pip** is Python’s **package installer**. It downloads code other people wrote (libraries) from the internet.

Check pip:

```bash
python3 -m pip --version
```

Windows:

```powershell
python -m pip --version
```

## Install a Package (Example)

We will use Pygame in Part 12. Preview:

```bash
python3 -m pip install pygame
```

For now, you do **not** need to install it yet.

## Create a Virtual Environment

In terminal, go to your project:

```bash
cd ~/Desktop/my_tetris
# or your actual path
```

Create the environment (folder `venv`):

```bash
python3 -m venv venv
```

Windows:

```powershell
python -m venv venv
```

A folder **`venv`** appears — do not edit files inside manually.

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

## Deactivate

```bash
deactivate
```

## requirements.txt (Good Habit)

List packages your project needs:

```
pygame>=2.5.0
```

Install everything listed:

```bash
pip install -r requirements.txt
```

We will add this when we reach Pygame.

## VS Code and venv

After creating `venv`, select interpreter:

**Python: Select Interpreter** → choose `./venv/bin/python` (path varies).

## Try It Yourself

1. Create `venv` inside `my_tetris`.
2. Activate it.
3. Run `pip list` — see installed packages (short list at first).
4. Deactivate.

## Summary

- **pip** installs third-party packages.
- **venv** isolates packages per project.
- **Activate** venv before `pip install` for Tetris.
- Next: learn `print` and comments in depth.

**Next:** [Output and Comments](../part3-basics/01-output-and-comments.html)
