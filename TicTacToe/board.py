import pygame
from .constants import *
import numpy as np


class Board:

    def __init__(self):
        self.board = np.zeros((ROWS, COLS))
        self.has_asc = False
        self.has_dec = False
        self.game_over = False

    def draw_grid(self, win, player, row=None, col=None):
        win.fill(WHITE)
        for _row in range(1, 3):
            pygame.draw.line(win, BLACK, (0, _row * 100), (WIDTH, _row * 100), 4)
            pygame.draw.line(win, BLACK, (_row * 100, 0), (_row * 100, HEIGHT), 4)

        self.draw_shape(win, player, row, col)

    def mark_square(self, row, col, player):
        if self.is_square_available(row, col):
            self.board[row][col] = player

    def is_square_available(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        return np.count_nonzero(self.board == 0) == 0

    def draw_shape(self, win, player,  row=None, col=None):
        for _row in range(ROWS):
            for _col in range(COLS):
                if self.board[_row][_col] == O:
                    pygame.draw.circle(win, RED, (int((_col * 100) + 50),
                                                  int((_row * 100) + 50)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[_row][_col] == X:
                    pygame.draw.line(win, BLUE, (_col * 100 + SPACE, _row * 100 + 50 - SPACE),
                                     (_col * 100 + 100 - SPACE, _row * 100 + 50 + SPACE), CROSS)
                    pygame.draw.line(win, BLUE, (_col * 100 + SPACE, _row * 100 + 50 + SPACE),
                                     (_col * 100 + 100 - SPACE, _row * 100 + 50 - SPACE), CROSS)

        self.who_wins(win, player, row, col)

    def who_wins(self, win, player, row, col):
        if self.has_vertical_line(player):

            self.draw_vertical_line(col, win)
            self.game_over = True

        elif self.has_horizontal_line(player):

            self.draw_horizontal_line(row, win)
            self.game_over = True

        elif self.is_diagonal_has_same_player(player):
           
            self.draw_diagonal_line(win)
            self.game_over = True

    def draw_vertical_line(self, col, win):

        posX = (col * 100) + 50
        pygame.draw.line(win, BLACK, (posX, 15), (posX, HEIGHT - 15), 15)

    def has_vertical_line(self, player):
        arr = self.board.sum(axis=0)
        for col in range(COLS):
            if arr[col] == player * 3:
                return True

        return False

    def draw_horizontal_line(self, row, win):
        posY = (row * 100) + 50
        pygame.draw.line(win, BLACK, (15, posY), (WIDTH - 15, posY), 15)

    def has_horizontal_line(self, player):
        arr = self.board.sum(axis=1)
        for row in range(ROWS):
            if arr[row] == player * 3:
                return True

        return False

    def draw_diagonal_line(self, win):

        if self.has_dec:
            pygame.draw.line(win, BLACK, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)
        else:
            pygame.draw.line(win, BLACK, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

    def is_diagonal_has_same_player(self, player):
        count = 0
        if self.board[1][1] == player:
            count += 1
            if self.board[0][0] == player:
                count += 1
                self.has_dec = True
            elif self.board[0][2] == player:
                count += 1
                self.has_dec = False
            if self.board[2][0] == player:
                count += 1
            elif self.board[2][2] == player:
                count += 1

            return count == 3

        return count == 3

    def restart(self, win):
        win.fill(WHITE)
        self.board = np.zeros((ROWS, COLS))
        self.draw_shape(win, 1)
