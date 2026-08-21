import random

from constants import WIDTH
from shapes import PIECE_LETTERS, SHAPES


class Piece:
    def __init__(self, name=None, rotation=0, row=0, col=None):
        self.name = name or random.choice(PIECE_LETTERS)
        self.rotation = rotation
        self.row = row
        self.col = col if col is not None else WIDTH // 2 - 2

    def cells(self):
        offsets = SHAPES[self.name][self.rotation]
        return [(self.row + dr, self.col + dc) for dr, dc in offsets]

    def move(self, d_row, d_col):
        self.row += d_row
        self.col += d_col

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4

    @classmethod
    def random_spawn(cls):
        return cls()
