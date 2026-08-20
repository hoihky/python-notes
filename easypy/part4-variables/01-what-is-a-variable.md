# Chapter 12: What Is a Variable?

A **variable** is a **named box** in memory that holds a value. Instead of repeating `5` everywhere, you store `5` in `piece_x` and read `piece_x` when drawing.

Think of your Tetris program as a notebook. Every number you need to remember — where the piece sits, how many points the player has, whether the game ended — gets written on a labeled line. That label is the variable name; what you wrote is the value.

## Analogy

| Real world | Programming |
|------------|-------------|
| Label on a storage bin | Variable **name** |
| Contents of the bin | **Value** |
| Replacing contents | **Assignment** |

When you play Tetris, the piece does not stay in one spot. You update the bin labeled `piece_x` instead of inventing a new label every frame. The name stays the same; only the contents change.

## What Happens When You Assign

When Python sees `score = 0`, it does two things:

1. Creates (or finds) a name in memory: `score`
2. Stores the value `0` under that name

Later, when you write `print(score)`, Python looks up the name and returns whatever is stored there right now.

```python
score = 0
print(score)  # expected output: 0
```

Read aloud: “score **gets** zero” or “score **equals** zero.” Both phrasings are fine — the important part is that `=` **stores**, it does not ask a question (that comes later with `==`).

## Using a Variable

```python
piece_x = 4
print(piece_x)  # expected output: 4
piece_x = 5
print(piece_x)  # expected output: 5
```

The **name** stays; the **value** can change. After the second assignment, the old value `4` is gone — `piece_x` now means `5`. There is no undo unless you assign again.

### Step-by-step walkthrough

Imagine the falling I-piece starts in column 4:

1. `piece_x = 4` — piece is in column 4
2. Player presses right — you will eventually write `piece_x += 1`
3. `piece_x` becomes 5 — same name, new position

You never need to rewrite your drawing code; it always reads `piece_x`.

## Variables Can Hold Different Types

```python
name = "Tetris"      # string — text in quotes
level = 1            # int — whole number
game_over = False    # boolean (True/False) — soon
```

Each type behaves differently. You add numbers with `+`, but `"Score: " + str(level)` needs conversion because text and numbers are not mixed with plain `+`.

Python variables are **not locked** to one type forever:

```python
x = 10
print(x)       # expected output: 10
x = "ten"
print(x)       # expected output: ten
```

This is allowed in Python (not in all languages). For Tetris, stick to one type per variable — `piece_x` should stay an integer so math like `piece_x + 1` always works.

## Multiple Variables

```python
piece_x = 4
piece_y = 0
shape = "I"
print(f"Shape {shape} at ({piece_x}, {piece_y})")
# expected output: Shape I at (4, 0)
```

In Tetris, `piece_x` and `piece_y` track where the falling block is. `shape` might hold `"I"`, `"O"`, `"T"`, and so on. Three separate variables beat one mystery number because each name tells you what it means.

## Variable Names Are for You

Python does not care about names — **you** do. Good names make code readable six months from now when you forget how collision worked.

| Clear | Unclear | Why it matters |
|-------|---------|----------------|
| `score` | `s` | `s` could mean score, speed, or shape |
| `board_width` | `w1` | `w1` gives no hint it is the board |
| `lines_cleared` | `x` | `x` sounds like a column, not a counter |

A teammate (or future you) should guess what a variable holds from its name alone.

## Reading vs Writing a Variable

| Action | Example | What happens |
|--------|---------|--------------|
| **Write** (assign) | `score = 100` | Stores 100 under `score` |
| **Read** (use) | `print(score)` | Looks up current value |
| **Read and write** | `score = score + 10` | Reads old value, adds 10, stores result |

The right side of `=` is always evaluated first. In `score = score + 10`, Python reads the old score, adds 10, then writes back to `score`.

## Constants (Convention)

Values that should not change during play:

```python
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
```

ALL_CAPS reminds you: do not reassign lightly. Python will not stop you from writing `BOARD_WIDTH = 99`, but your wall checks would break. Treat ALL_CAPS names as promises: “this never changes mid-game.”

## Common Mistakes

**Using a variable before assigning it**

```python
print(piece_x)  # NameError — piece_x does not exist yet
piece_x = 4
```

Always assign before you read.

**Confusing the name with the value**

```python
piece_x = 4
# Wrong mental model: "the name 4"
# Right mental model: "piece_x currently holds 4"
```

**Copy-pasting magic numbers**

```python
# Hard to maintain
if column < 10:
    draw_at(column, 0)

# Better — one place to change board size
if column < BOARD_WIDTH:
    draw_at(column, 0)
```

## Try It Yourself

```python
player_name = "You"
score = 0
lines = 0
print(f"{player_name}: {score} points, {lines} lines")
# expected output: You: 0 points, 0 lines

score = 100
print(f"{player_name}: {score} points")
# expected output: You: 100 points
```

Extend the exercise: add `level = 1`, assign `lines = 4`, and print all three variables on one line with an f-string.

## Summary

- **Variables** store values under names.
- Values can **change** with assignment; names usually stay fixed.
- Tetris uses variables for **position**, **score**, **game state**, and **shape**.
- Good names save you from guessing; ALL_CAPS marks values that should not change.
- Next: naming rules and assignment details.

**Next:** [Naming and Assignment](02-naming-and-assignment.md)
