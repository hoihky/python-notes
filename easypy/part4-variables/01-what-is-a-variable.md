---
title: What Is a Variable?
order: 1
---

# Chapter 12: What Is a Variable?

A **variable** is a **named box** in memory that holds a value. Instead of repeating `5` everywhere, you store `5` in `piece_x` and read `piece_x` when drawing.

## Analogy

| Real world | Programming |
|------------|-------------|
| Label on a storage bin | Variable **name** |
| Contents of the bin | **Value** |
| Replacing contents | **Assignment** |

```python
score = 0
```

Read aloud: “score **gets** zero” or “score **equals** zero.”

## Using a Variable

```python
piece_x = 4
print(piece_x)
piece_x = 5
print(piece_x)
```

The **name** stays; the **value** can change.

## Variables Can Hold Different Types

```python
name = "Tetris"      # string
level = 1            # int
game_over = False    # boolean (True/False) — soon
```

Python variables are **not locked** to one type forever:

```python
x = 10
x = "ten"  # allowed in Python (not in all languages)
```

## Multiple Variables

```python
piece_x = 4
piece_y = 0
shape = "I"
```

In Tetris, `piece_x` and `piece_y` track where the falling block is.

## Variable Names Are for You

Python does not care about names — **you** do. Good names make code readable.

| Clear | Unclear |
|-------|---------|
| `score` | `s` |
| `board_width` | `w1` |
| `lines_cleared` | `x` |

## Constants (Convention)

Values that should not change during play:

```python
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
```

ALL_CAPS reminds you: do not reassign lightly.

## Try It Yourself

```python
player_name = "You"
score = 0
lines = 0
print(f"{player_name}: {score} points, {lines} lines")
score = 100
print(f"{player_name}: {score} points")
```

## Summary

- **Variables** store values under names.
- Values can **change** with assignment.
- Tetris uses variables for **position**, **score**, **game state**.
- Next: naming rules and assignment details.

**Next:** [Naming and Assignment](02-naming-and-assignment.html)
