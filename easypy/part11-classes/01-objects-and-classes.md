# Chapter 36: Introduction to Classes and Objects

A **class** is a **blueprint**; an **object** is one **thing** built from that blueprint. In Tetris, a **Piece** can be an object with its own row, column, and shape.

Up to now, your game state lived in a dictionary — `state["piece_row"]`, `state["score"]`, and so on. That works. But as games grow, grouping related data and actions into **objects** makes code easier to read and harder to break.

## Real-World Analogy

| Blueprint | Objects |
|-----------|---------|
| Cookie cutter | Each cookie |
| Car design | Your car, my car |
| `Piece` class | Current piece, next piece |

The cookie cutter is not a cookie — it describes how to make one. Each time you press dough, you get a new cookie (object) with the same shape rules but its own position on the tray.

In Tetris terms: one `Piece` **class** defines what every piece knows and can do. Each falling piece is its **own** object with its own row, column, and rotation.

## Simple Class

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido")
fido.bark()
# expected output: Fido says woof!
```

Breaking down the syntax:

- **`class Dog`** — defines a new type named `Dog`.
- **`__init__`** — constructor; runs automatically when you call `Dog(...)`.
- **`self`** — the object itself; every method receives it as the first parameter.
- **`self.name`** — attribute (data stored on the object).
- **`bark`** — method (function that belongs to the object).

Two dogs can share the same class but have different names:

```python
a = Dog("Ada")
b = Dog("Basil")
a.bark()  # Ada says woof!
b.bark()  # Basil says woof!
```

## self Explained

`self` lets methods access this object's data:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

c = Counter()
c.increment()
c.increment()
print(c.value)  # 2
```

When you write `c.increment()`, Python passes `c` as `self` behind the scenes. Inside `increment`, `self.value` means "this counter's value," not some global variable.

Without `self`, methods would not know **which** object's data to change — imagine two counters sharing one `value` variable by mistake.

## Attributes vs Methods

| Kind | Purpose | Example |
|------|---------|---------|
| Attribute | Stores data | `self.name`, `self.score` |
| Method | Does something | `self.bark()`, `self.move_down()` |

Good design puts data and the actions that use that data in the same class. A piece's row should change through a piece method, not random code elsewhere.

## Why Classes for Tetris?

Instead of scattering piece facts across a dictionary:

```python
state["piece_row"]
state["piece_col"]
state["name"]
state["rotation"]
```

You can write:

```python
piece.row
piece.col
piece.name
piece.rotation
piece.move_down()
```

Data and actions live **together**. When you debug "why did the piece jump?", you look at the `Piece` class instead of hunting keys in a giant dict.

Classes also help your editor suggest names — typing `piece.` can show available methods.

## A tiny Tetris-flavored preview

Not the full game yet — just the idea:

```python
class FallingBlock:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move_down(self):
        self.row += 1

block = FallingBlock(0, 4)
block.move_down()
print(block.row)  # 1
```

The next chapter replaces this sketch with a real `Piece` tied to `SHAPES`.

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Forgetting `self` in method definition | Error when calling method | First parameter must be `self` |
| Using `self` outside a class method | NameError | `self` only exists inside class methods |
| Same attribute name on class and instance | Confusing shared vs per-object data | Put instance data on `self` in `__init__` |
| Creating objects without `__init__` args | Missing required data | Pass spawn values when constructing |

## Try It Yourself

Create `class Player` with `name` and `score`, method `add_points(n)`:

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, n):
        self.score += n

    def __str__(self):
        return f"{self.name}: {self.score} pts"

p = Player("Alex")
p.add_points(100)
p.add_points(300)
print(p)  # Alex: 400 pts
```

Add a method `reset_score()` and test it. Then imagine mapping `Player` to Tetris — same pattern as score tracking in your game.

## Summary

- **Class** = blueprint; **object** = instance built from it.
- **`__init__`** sets up attributes when the object is created.
- **`self`** refers to the current object inside methods.
- Classes group related data and behavior — perfect for pieces and games.
- Next: **`Piece` class**.

**Next:** [A Piece Class for Tetris](02-piece-class.md)
