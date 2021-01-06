from .constants import *
from .Drawing import *
import numpy as np
import time
import math
import random as rn


class Board:

    def __init__(self, win):
        self.board = np.zeros((ROWS, COLS))
        self.game_over = False
        self.turn = X
        self.depth = 0
        self._score = 0
        self.drawing = Drawing(win)

    def mark_square(self, win, row, col, player):

        if self.is_square_available(row, col):
            self.board[row][col] = player
            self.turn = O
            self.drawing.draw_shape(win, self.board)
            self.who_wins(win, player, row, col)
            pygame.display.update()

        best = self.minimax(win, self.board, 0, O, row, col)
        print("best", best)

        while True:
            if self.is_square_available(best[0], best[1]):
                self.board[best[0]][best[1]] = O
                self.drawing.draw_shape(win, self.board)
                self.who_wins(win, O, best[0], best[1])
                pygame.display.update()

                break
            else:
                best = self.minimax(win, self.board, 0, O, row, col)

        self.turn = X

    def is_square_available(self, row, col):
        return self.board[row][col] == 0

    def is_board_full(self):
        return np.count_nonzero(self.board == 0) == 0

    def who_wins(self, win, player, row, col):

        if self.has_vertical_line(player):

            self.drawing.draw_vertical_line(col, win)
            self._score = player
            self.game_over = True

        elif self.has_horizontal_line(player):
            self.drawing.draw_horizontal_line(row, win)
            self.game_over = True
            self._score = player

        elif self.is_diagonal_has_same_player(player):
            self.drawing.draw_diagonal_line(win)
            self.game_over = True
            self._score = player

        elif self.is_board_full():
            self.game_over = True
            self._score = TOE
        else:
            self.game_over = False
            self._score = TOE

    def check_winner(self, player):

        if self.has_vertical_line(player):
            self.game_over = True
            return player

        elif self.has_horizontal_line(player):
            self.game_over = True
            return player

        elif self.is_diagonal_has_same_player(player):
            self.game_over = True
            return player

        elif self.is_board_full():
            self.game_over = True
            return TOE
        else:
            self.game_over = False
            return TOE

    def has_vertical_line(self, player):
        arr = self.board.sum(axis=0)
        for col in range(COLS):
            if arr[col] == player * 3:  # -3 or 3
                return True

        return False

    def has_horizontal_line(self, player):
        arr = self.board.sum(axis=1)
        for row in range(ROWS):
            if arr[row] == player * 3:
                return True

        return False

    def is_diagonal_has_same_player(self, player):

        if self.board[1][1] == player and self.board[0][0] == player and self.board[2][2] == player:
            self.drawing.has_dec = True
            return True

        elif self.board[1][1] == player and self.board[0][2] == player and self.board[2][0] == player:
            self.drawing.has_dec = False
            return True
        else:
            return False

    def restart(self, win):
        win.fill(WHITE)
        self.board = np.zeros((ROWS, COLS))
        self.turn = X
        self.drawing.draw_grid(win)
        self.drawing.draw_shape(win, self.board)
        self.game_over = False

    # --------------------------------------------------------------

    # an AI approach

    def get_empty_cells(self):
        empty = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    empty.append([row, col])
        return empty

    def minimax(self, win, state, depth, player, row, col):

        if player == O:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, +math.inf]

        self._score = self.check_winner(player)
        if depth == 9 or self.game_over:
            # print("self._score", self._score)
            return [-1, -1, self._score]

        for cell in self.get_empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(win, state, depth + 1, -player, row, col)
            # print ("score", score)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == O:
                best = max(score[2], best[2])
            else:
                best = min(score[2], best[2])

        # print("best", best)
        return best


# --------------------------------------------------------------


'''
 count = 0
        if not self.is_board_full() and self._score == 0:
            if self.board[1][1] == X and len(self.get_empty_cells()) == 8:
                pick = rn.choice([[0,0],[0,2], [2,0],[2,2]])
                self.board[pick[0]][pick[1]] = O

                return

            elif self.board[1][1] == 0:
                self.board[1][1] = O

            else:
                if sum(self.board[0][:]) ==2 or sum(self.board[0][:]) == -2:
                    for col in range(COLS):
                        if self.is_square_available(0,col):
                            self.board[0][col] = O
                            break
                elif sum(self.board[1][:]) == 2 or  sum(self.board[1][:]) == -2:
                    for col in range(COLS):
                        if self.is_square_available(1, col):
                            self.board[0][col] = O
                            break
                elif sum(self.board[2][:]) == 2 or sum(self.board[2][:]) == -2:
                    for col in range(COLS):
                        if self.is_square_available(2, col):
                            self.board[0][col] = O
                            break
                elif sum(self.board[:][0]) == 2 or sum(self.board[:][0]) == -2:
                    for row in range(ROWS):
                        if self.is_square_available(row, 0):
                            self.board[0][row] = O
                            break

                elif sum(self.board[:][1]) == 2 or sum(self.board[:][1]) == -2:
                    for row in range(ROWS):
                        if self.is_square_available(row, 1):
                            self.board[1][row] = O
                            break

                elif sum(self.board[:][2]) == 2 or sum(self.board[:][2]) == -2:
                    for row in range(ROWS):
                        if self.is_square_available(row, 1):
                            self.board[1][row] = O
                            break

                elif self.board[1][1] == X:
                    count += 1
                    if self.board[0][0] == X:
                        count += 1
                        self.has_dec = True
                    elif self.board[0][2] == X:
                        count += 1
                        self.has_dec = False
                    if self.board[2][0] == X:
                        count += 1
                    elif self.board[2][2] == X:
                        count += 1

                if count >=2:
                    if self.has_dec:
                        if self.is_square_available(0,0):
                            self.board[0][0] = O
                        else:
                            self.board[2][2] = O

                    else:
                        if self.is_square_available(0, 2):
                            self.board[0][2] = O
                        else:
                            self.board[2][0] = O
                else:
                    pick = rn.choice(self.get_empty_cells())
                    self.board[pick[0]][pick[1]] = O



 '''
