---
title: Introduction to Classes and Objects
order: 1
---

# Chapter 36: Introduction to Classes and Objects

A **class** is a **blueprint**; an **object** is one **thing** built from that blueprint. In Tetris, a **Piece** can be an object with its own row, column, and shape.

## Real-World Analogy

| Blueprint | Objects |
|-----------|---------|
| Cookie cutter | Each cookie |
| Car design | Your car, my car |
| `Piece` class | Current piece, next piece |

## Simple Class

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

fido = Dog("Fido")
fido.bark()
```

- **`class Dog`** — defines type
- **`__init__`** — constructor, runs when object created
- **`self`** — the object itself
- **`self.name`** — attribute (data)
- **`bark`** — method (function on object)

## self Explained

`self` lets methods access this object's data:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

c = Counter()
c.increment()
print(c.value)  # 1
```

## Why Classes for Tetris?

Instead of:

```python
state["piece_row"]
state["piece_col"]
state["name"]
```

You can write:

```python
piece.row
piece.col
piece.name
piece.move_down()
```

Data and actions live **together**.

## Try It Yourself

Create `class Player` with `name` and `score`, method `add_points(n)`.

## Summary

- **Class** = blueprint; **object** = instance.
- **`__init__`** sets up attributes.
- **`self`** refers to current object.
- Next: **`Piece` class**.

**Next:** [A Piece Class for Tetris](02-piece-class.html)
