---
title: Install Python
order: 1
---

# Chapter 4: Install Python

Before writing code, you need **Python** on your computer. This chapter walks through installation on **Windows**, **macOS**, and **Linux**.

## Download the Official Installer

Always use the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Click the big **Download Python 3.x.x** button (any 3.10+ version is fine).

## Windows

1. Run the downloaded `.exe` installer.
2. **Important:** Check **“Add python.exe to PATH”** at the bottom of the first screen.
3. Click **Install Now**.
4. When finished, click **Close**.

### Verify on Windows

Open **Command Prompt** or **PowerShell**:

```powershell
python --version
```

You should see something like `Python 3.12.4`.

If `python` fails, try:

```powershell
py --version
```

## macOS

### Option A — Official installer

1. Download the macOS installer from python.org.
2. Run the `.pkg` and follow prompts.

### Option B — Homebrew (if you use Homebrew)

```bash
brew install python
```

### Verify on macOS

Open **Terminal**:

```bash
python3 --version
```

On Mac, use `python3` (not always `python`).

## Linux (Ubuntu / Debian)

Python 3 is often pre-installed:

```bash
python3 --version
```

If missing:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## What Got Installed?

| Component | Purpose |
|-----------|---------|
| `python` / `python3` | Runs your programs |
| **pip** | Downloads extra libraries (e.g. Pygame later) |
| **IDLE** | Simple built-in editor (optional; we use VS Code) |

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| “command not found” | Reinstall; check PATH (Windows) |
| Wrong version (2.x) | Use `python3` explicitly |
| Microsoft Store Python | OK for learning; or use python.org build |

## Try It Yourself

Run `python3 --version` (or `python --version` on Windows). Screenshot or write the version in `my_tetris/notes.txt`.

## Summary

- Install **Python 3** from python.org.
- On Windows, enable **Add to PATH**.
- Verify with `--version`.
- Next: choose an editor to write code comfortably.

**Next:** [Editor and Development Tools](02-editor-and-tools.html)
