# Chapter 16: if and else

**if** lets Python **choose** which code runs. Without it, Tetris could not check walls or clear lines.

So far every line ran top to bottom. With `if`, Python skips blocks when the condition is **False** — like a guard that only opens the door when the answer is yes.

## Basic if

```python
score = 1500
if score >= 1000:
    print("Great job!")
# expected output: Great job!
```

Structure:

```python
if condition:
    indented_line
    another_indented_line
```

- **Colon** `:` after condition
- **Indented** block (4 spaces — VS Code helps)

If `condition` is **False**, Python **skips** the block entirely — no error, no message, just silence.

```python
score = 50
if score >= 1000:
    print("Great job!")
print("Done")
# expected output: Done  (only — the if body never ran)
```

## else

When you need “otherwise”:

```python
command = input("Move (a/d): ")
if command == "a":
    print("Moving left")
else:
    print("Not left")
```

If the player types `a`, you see “Moving left”. Any other key hits `else`. There is no third path unless you add `elif`.

## elif — Multiple Choices

```python
command = input("Move: ")
if command == "a":
    print("Left")
elif command == "d":
    print("Right")
elif command == "s":
    print("Down")
else:
    print("Unknown")
```

Python checks top to bottom and runs **only the first matching block**. Order matters: put specific cases before general ones.

Tetris command handler will look like this — one `input`, many branches, one action per key.

### Walkthrough — scoring by lines cleared

```python
lines = 2

if lines == 0:
    print("No bonus")
elif lines == 1:
    print("+100")
elif lines == 4:
    print("TETRIS bonus!")
else:
    print("+200 combo")

# expected output: +200 combo
```

`lines == 4` is checked only if earlier branches failed — with `lines = 2`, neither `0`, `1`, nor `4` matched, so `else` runs.

## Nested if

```python
game_over = False
BOARD_WIDTH = 10
piece_x = 8

if not game_over:
    if piece_x < BOARD_WIDTH - 1:
        piece_x += 1
        print("Moved to", piece_x)
    else:
        print("Wall blocked move")

# expected output: Moved to 9
```

Outer `if` checks the game is active; inner `if` checks the wall. Both must pass to move. Deep nesting gets hard to read — later you will combine conditions with `and`.

## Tetris — Wall Check

```python
BOARD_WIDTH = 10
piece_x = 8

if piece_x + 1 < BOARD_WIDTH:
    piece_x += 1
    print("Moved right to", piece_x)
else:
    print("Blocked by wall")
# expected output: Moved right to 9
```

Run again with `piece_x = 9` — you should see “Blocked by wall” and `piece_x` stays 9.

## Tetris — Game Over Check

```python
piece_y = 0
game_over = False

if piece_y <= 0:
    game_over = True
    print("Game Over!")
# expected output: Game Over!
```

(Exact rules refined when we build the board.) New-piece spawn above the visible area might use `piece_y < 0` instead — the pattern is the same: **test → set flag → message**.

## Empty Blocks — pass

Sometimes you need a placeholder:

```python
if game_over:
    pass  # do nothing yet — stub for later
else:
    print("Still playing")
```

`pass` is a no-op — useful while sketching structure.

## Indentation Errors

```python
if True:
print("wrong")  # IndentationError
```

Always indent the block under `if`. Mixing tabs and spaces causes painful errors — stick to 4 spaces.

### Common mistake — no colon

```python
# if score > 0   # SyntaxError — missing colon
if score > 0:
    print(score)
```

## Common Mistakes

**Using `if` when both branches should run**

Only one branch of `if` / `elif` / `else` executes per test. To run two independent checks, use two separate `if` statements.

**Assignment instead of comparison**

```python
# if command = "q":  # SyntaxError
if command == "q":
    print("Quit")
```

**Forgetting to update state inside the branch**

```python
if command == "d":
    print("Right")
    # piece_x += 1  # easy to forget — piece never moves
```

## Try It Yourself

```python
lines = int(input("Lines cleared this turn: "))
if lines == 0:
    print("Keep going!")
elif lines == 1:
    print("Single!")
elif lines >= 4:
    print("TETRIS!")
else:
    print("Nice combo!")
```

Try inputs `0`, `1`, `2`, and `4` and note which branch fires. With `4`, `elif lines >= 4` runs — not `else`.

## Summary

- **`if`** runs code only when condition is True.
- **`else`** / **`elif`** handle other cases — first match wins.
- **Indentation** defines blocks; colons are required.
- Tetris uses `if` for movement, collision, scoring messages, and game over.
- Next: combining conditions with **and**, **or**, **not**.

**Next:** [Combining Conditions](03-combining-conditions.md)
