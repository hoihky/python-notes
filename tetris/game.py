from board import draw_board, is_row_full, make_board
from collision import can_place
from constants import BLOCK, EMPTY, HEIGHT, POINTS, WIDTH
from piece import Piece


def clear_full_lines(board):
    new_board = []
    cleared = 0
    for row in board:
        if is_row_full(row):
            cleared += 1
        else:
            new_board.append(row)
    while len(new_board) < HEIGHT:
        new_board.insert(0, [EMPTY] * WIDTH)
    return new_board, cleared


class Game:
    def __init__(self):
        self.board = make_board()
        self.piece = Piece.random_spawn()
        self.score = 0
        self.lines = 0
        self.game_over = False
        if not self.can_place_current():
            self.game_over = True

    def can_place_current(self):
        return can_place(self.board, self.piece.cells())

    def draw(self):
        draw_board(
            self.board,
            self.piece.cells(),
            self.score,
            self.lines,
            self.piece.name,
        )

    def handle(self, cmd):
        if cmd == "q":
            self.game_over = True
        elif cmd == "a":
            self.try_move(0, -1)
        elif cmd == "d":
            self.try_move(0, 1)
        elif cmd == "w":
            self.try_rotate()
        elif cmd == "s":
            self.try_move(1, 0)
        elif cmd == "h":
            self.hard_drop()

    def try_move(self, dr, dc):
        self.piece.move(dr, dc)
        if not self.can_place_current():
            self.piece.move(-dr, -dc)
            return False
        return True

    def try_rotate(self):
        old_rot = self.piece.rotation
        self.piece.rotate()
        if not self.can_place_current():
            self.piece.rotation = old_rot
            return False
        return True

    def tick(self):
        if not self.try_move(1, 0):
            self.lock_and_spawn()

    def hard_drop(self):
        while self.try_move(1, 0):
            pass
        self.lock_and_spawn()

    def lock_and_spawn(self):
        for r, c in self.piece.cells():
            if r >= 0:
                self.board[r][c] = BLOCK

        new_board, cleared = clear_full_lines(self.board)
        self.board = new_board
        if cleared:
            self.lines += cleared
            self.score += POINTS.get(cleared, cleared * 100)

        self.piece = Piece.random_spawn()
        if not self.can_place_current():
            self.game_over = True


def main():
    game = Game()
    print("Welcome to Text Tetris!")
    print("Controls: a/d move, s drop, w rotate, h hard drop, q quit")

    while not game.game_over:
        game.draw()
        cmd = input("> ").strip().lower()
        game.handle(cmd)
        if not game.game_over:
            game.tick()

    game.draw()
    print(f"Game Over! Final score: {game.score}")
    print(f"Lines cleared: {game.lines}")
    if game.lines >= 4:
        print("Nice work — you cleared multiple lines!")


if __name__ == "__main__":
    main()
