# Chapter 18: while Loops

A **loop** repeats code. **`while`** repeats **as long as** a condition is True — perfect for “keep playing until game over.”

Without loops you would copy-paste the same move-and-draw code hundreds of times. The game loop is one `while` block that runs until `game_over` becomes True.

## Basic while

```python
count = 0
while count < 5:
    print("Count is", count)
    count += 1
print("Done")
```

Expected output:

```
Count is 0
Count is 1
Count is 2
Count is 3
Count is 4
Done
```

Each trip through the loop is an **iteration**. The condition is checked **before** every iteration — if it is False on entry, the body never runs.

## Flow

```mermaid
flowchart TD
    Start([Start]) --> Check{condition True?}
    Check -->|Yes| Body[Run loop body]
    Body --> Check
    Check -->|No| End([Continue after loop])
```

Trace `count`: starts 0, prints, becomes 1, … until `count < 5` fails when `count` is 5.

## Infinite Loop Danger

```python
# while True:
#     print("Forever")  # only stop with Ctrl+C
```

Always ensure something inside **changes** the condition or **breaks**. Forgetting `count += 1` in the basic example would print “Count is 0” forever.

Safe pattern:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # must move toward ending the loop
```

## break — Exit Early

```python
while True:
    cmd = input("Command (q=quit): ")
    if cmd == "q":
        break
    print("You typed:", cmd)
```

`break` jumps out of the **innermost** loop immediately — even if the condition is still True. Tetris might `break` from an input loop when the player quits.

## continue — Skip Rest of Iteration

```python
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
# expected output: 1, 2, 4, 5 (each on its own line) — skips 3
```

`continue` goes straight to the next condition check — nothing below it in that iteration runs. Useful to skip invalid input without exiting the whole loop.

## else on while (Rare)

If the loop finishes without `break`, an optional `else` runs:

```python
n = 0
while n < 3:
    n += 1
else:
    print("Finished normally")
# expected output: Finished normally
```

You will see this rarely in games — but it is valid Python.

## Tetris Game Loop (Skeleton)

```python
game_over = False
piece_y = 0

while not game_over:
    print(f"Piece row: {piece_y}")
    cmd = input("Move (s=down, q=quit): ")
    if cmd == "q":
        game_over = True
    elif cmd == "s":
        piece_y += 1
        if piece_y >= 19:
            game_over = True
            print("Hit bottom — game over")
```

Real Tetris adds board, collision, new pieces. The skeleton shows the rhythm: **show state → read input → update variables → check end**.

### What each iteration does

1. Print current row — feedback for the player
2. Read a command — `s` or `q`
3. Update `piece_y` or set `game_over`
4. Loop checks `not game_over` again

## Counter vs Sentinel

| Style | Example | When |
|-------|---------|------|
| **Counter** | `while count < 5` | Known number of repeats |
| **Sentinel** | `while not game_over` | Run until a flag changes |

Tetris main loop is sentinel-style — you do not know how many turns the match will last.

## Common Mistakes

**Infinite loop — condition never becomes False**

```python
score = 0
while score < 500:
    print(score)
    # forgot score += 100 — prints 0 forever
```

**Updating the wrong variable**

```python
piece_y = 0
while piece_y < 5:
    y = piece_y + 1  # updates y, not piece_y — infinite loop at 0
```

**Off-by-one in condition**

```python
# rows 0..4 — five rows
while piece_y <= 5:  # one too many if you wanted 0..4 only
    piece_y += 1
```

## Try It Yourself

Write a loop that:

1. Starts `score = 0`
2. Each iteration adds 100 to score and prints it
3. Stops when `score >= 500`

Expected output:

```
100
200
300
400
500
```

Bonus: count iterations with `turns = 0` and `turns += 1` each pass; print turns at the end.

## Summary

- **`while condition:`** repeats while True — check happens before each body run.
- **`break`** exits loop; **`continue`** skips to next iteration.
- Always ensure the condition can eventually become False (unless you mean `while True` with `break`).
- Tetris **main loop** runs until `game_over`.
- Next: **`for`** loops.

**Next:** [for Loops and range](02-for-loops.md)
