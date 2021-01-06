import pygame
from .constants import *


class Drawing:

    def __init__(self, win):
        self.has_asc = False
        self.has_dec = False
        self.draw_grid(win)

    def draw_grid(self, win):
        for _row in range(1, 3):
            pygame.draw.line(win, BLACK, (0, _row * 100), (WIDTH, _row * 100), 4)
            pygame.draw.line(win, BLACK, (_row * 100, 0), (_row * 100, HEIGHT), 4)

    def draw_shape(self, win, board):

        for _row in range(ROWS):
            for _col in range(COLS):
                if board[_row][_col] == O:
                    pygame.draw.circle(win, RED, (int((_col * 100) + 50),
                                                  int((_row * 100) + 50)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif board[_row][_col] == X:
                    pygame.draw.line(win, BLUE, (_col * 100 + SPACE, _row * 100 + 50 - SPACE),
                                     (_col * 100 + 100 - SPACE, _row * 100 + 50 + SPACE), CROSS)
                    pygame.draw.line(win, BLUE, (_col * 100 + SPACE, _row * 100 + 50 + SPACE),
                                     (_col * 100 + 100 - SPACE, _row * 100 + 50 - SPACE), CROSS)

    def draw_vertical_line(self, col, win):

        posX = (col * 100) + 50
        pygame.draw.line(win, BLACK, (posX, 15), (posX, HEIGHT - 15), 15)

    def draw_horizontal_line(self, row, win):
        posY = (row * 100) + 50
        pygame.draw.line(win, BLACK, (15, posY), (WIDTH - 15, posY), 15)

    def draw_diagonal_line(self, win):

        if self.has_dec:
            pygame.draw.line(win, BLACK, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)
        else:
            pygame.draw.line(win, BLACK, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)