"""Color Tetris with Pygame — entry point for the graphical version (Easy Python Part 12)."""

import pygame

from constants import HEIGHT, WIDTH
from game import Game

CELL = 30
SCREEN_W = CELL * WIDTH + 200
SCREEN_H = CELL * HEIGHT

COLORS = {
    ".": (40, 40, 50),
    "#": (200, 200, 220),
    "I": (0, 240, 240),
    "O": (240, 240, 0),
    "T": (160, 0, 240),
    "S": (0, 240, 0),
    "Z": (240, 0, 0),
    "J": (0, 0, 240),
    "L": (240, 160, 0),
}

BACKGROUND = (20, 20, 30)
HUD_COLOR = (220, 220, 220)


def draw_cell(screen, row, col, color):
    x = col * CELL
    y = row * CELL
    pygame.draw.rect(screen, color, (x, y, CELL - 1, CELL - 1))


def draw_board_gui(screen, board, piece):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            color = COLORS.get(cell, COLORS["#"])
            draw_cell(screen, r, c, color)
    for r, c in piece.cells():
        if r >= 0:
            draw_cell(screen, r, c, COLORS.get(piece.name, (255, 255, 255)))


def draw_hud(screen, font, game, fall_speed):
    x = WIDTH * CELL + 20
    score_text = font.render(f"Score: {game.score}", True, HUD_COLOR)
    lines_text = font.render(f"Lines: {game.lines}", True, HUD_COLOR)
    piece_text = font.render(f"Piece: {game.piece.name}", True, HUD_COLOR)
    speed_text = font.render(f"Fall: {fall_speed}ms", True, HUD_COLOR)
    screen.blit(score_text, (x, 20))
    screen.blit(lines_text, (x, 50))
    screen.blit(piece_text, (x, 80))
    screen.blit(speed_text, (x, 110))
    controls = font.render("Arrows move/rotate", True, HUD_COLOR)
    screen.blit(controls, (x, 150))
    screen.blit(font.render("Down: soft drop", True, HUD_COLOR), (x, 175))
    screen.blit(font.render("Space: hard drop", True, HUD_COLOR), (x, 200))
    screen.blit(font.render("Q: quit", True, HUD_COLOR), (x, 225))


def run_gui():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Easy Python Tetris")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    game = Game()
    fall_timer = 0

    running = True
    while running:
        fall_speed = max(100, 500 - game.lines * 20)
        dt = clock.tick(60)
        fall_timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.handle("a")
                elif event.key == pygame.K_RIGHT:
                    game.handle("d")
                elif event.key == pygame.K_DOWN:
                    game.handle("s")
                elif event.key == pygame.K_UP:
                    game.handle("w")
                elif event.key == pygame.K_SPACE:
                    game.hard_drop()
                elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

        if fall_timer >= fall_speed:
            if not game.game_over:
                game.tick()
            fall_timer = 0

        screen.fill(BACKGROUND)
        draw_board_gui(screen, game.board, game.piece)
        draw_hud(screen, font, game, fall_speed)
        pygame.display.flip()

        if game.game_over:
            game_over_text = font.render("Game Over!", True, (240, 80, 80))
            screen.blit(game_over_text, (WIDTH * CELL + 20, 260))
            final_score = font.render(f"Score: {game.score}", True, HUD_COLOR)
            screen.blit(final_score, (WIDTH * CELL + 20, 290))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

    pygame.quit()


if __name__ == "__main__":
    run_gui()
