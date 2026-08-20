# Chapter 4: Install Python

Before writing code, you need **Python** on your computer. This chapter walks through installation on **Windows**, **macOS**, and **Linux**.

Installation is a one-time setup. After this chapter, you will verify Python works, note your version in `my_tetris/notes.txt`, and move on to picking an editor. Take your time on the Windows PATH step — it prevents the most common beginner headache.

## Download the Official Installer

Always use the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Click the big **Download Python 3.x.x** button (any 3.10+ version is fine).

Avoid random download sites that bundle extra toolbars or unrelated software. The python.org installer is the standard choice for learning and matches what most tutorials assume.

## Windows

1. Run the downloaded `.exe` installer.
2. **Important:** Check **"Add python.exe to PATH"** at the bottom of the first screen.
3. Click **Install Now**.
4. When finished, click **Close**.

**PATH** is a list of folders Windows searches when you type a command. If Python is not on PATH, the terminal cannot find `python` even though it is installed. Checking that box fixes this for most people.

### Verify on Windows

Open **Command Prompt** or **PowerShell**:

```powershell
python --version
# expected output example: Python 3.12.4
```

You should see something like `Python 3.12.4`.

If `python` fails, try:

```powershell
py --version
# expected output example: Python 3.12.4
```

The `py` launcher is another way to start Python on Windows. Either `python` or `py` is fine as long as the version starts with **3.10** or higher.

## macOS

### Option A — Official installer

1. Download the macOS installer from python.org.
2. Run the `.pkg` and follow prompts.

### Option B — Homebrew (if you use Homebrew)

```bash
brew install python
```

Homebrew is a package manager for developers on Mac. If you already use it, this is convenient. If you have never heard of Homebrew, Option A is simpler.

### Verify on macOS

Open **Terminal**:

```bash
python3 --version
# expected output example: Python 3.12.4
```

On Mac, use `python3` (not always `python`).

macOS may ship an older system Python. Always prefer the version you installed from python.org or Homebrew, and call it with `python3`.

## Linux (Ubuntu / Debian)

Python 3 is often pre-installed:

```bash
python3 --version
# expected output example: Python 3.10.12
```

If missing:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

The `python3-venv` package matters later when we create a virtual environment for Pygame. Installing it now saves a confusing error message in Part 2, Chapter 7.

## What Got Installed?

| Component | Purpose |
|-----------|---------|
| `python` / `python3` | Runs your programs |
| **pip** | Downloads extra libraries (e.g. Pygame later) |
| **IDLE** | Simple built-in editor (optional; we use VS Code) |

You can ignore IDLE for this tutorial. We use VS Code or Cursor for editing and the integrated terminal for running code.

### Quick check: pip works too

```bash
python3 -m pip --version
# expected output example: pip 24.0 from ... (python 3.12)
```

If pip is missing on Linux, install the `python3-pip` package from your distribution's repository.

## Step-by-step: first run after install

1. Open a terminal (Command Prompt, PowerShell, or Terminal app).
2. Run `python3 --version` or `python --version`.
3. If you see Python 3.10+, type `python3` (or `python`) and press Enter.
4. You should see `>>>` — the interactive shell from Chapter 2.
5. Type `print("Python works")` and press Enter.
6. Type `exit()` or press `Ctrl+D` (Mac/Linux) / `Ctrl+Z` then Enter (Windows) to leave.

That five-minute check confirms install **and** teaches you how to open the shell.

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| "command not found" | Reinstall; check PATH (Windows) |
| Wrong version (2.x) | Use `python3` explicitly |
| Microsoft Store Python | OK for learning; or use python.org build |

### Windows PATH still broken?

1. Uninstall Python from Settings → Apps.
2. Re-run the installer from python.org.
3. Check **Add python.exe to PATH** before Install Now.
4. Close and reopen the terminal (old windows do not pick up PATH changes).

### macOS: `python` opens Python 2

Use `python3` in all commands for this tutorial. You can create an alias later; for now, consistency matters more than convenience.

## Common Mistakes

| Mistake | Why it hurts | Fix |
|---------|--------------|-----|
| Skipping PATH on Windows | Terminal never finds Python | Reinstall with PATH checked |
| Mixing `python` and `python3` randomly | Runs wrong version | Pick one command; note it in `notes.txt` |
| Installing Python 2 tutorials | Outdated syntax | Confirm version is 3.10+ |

## Try It Yourself

Run `python3 --version` (or `python --version` on Windows). Screenshot or write the version in `my_tetris/notes.txt`.

Also write which command worked on your machine (`python` vs `python3`). Future chapters assume you know your own setup.

## Summary

- Install **Python 3** from python.org.
- On Windows, enable **Add to PATH**.
- Verify with `--version`.
- Next: choose an editor to write code comfortably.

**Next:** [Editor and Development Tools](02-editor-and-tools.md)
