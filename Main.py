import pygame
from TicTacToe import *
from TicTacToe.board import Board
import time

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN)
    WIN.fill(WHITE)
    board.drawing.draw_grid(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if board.game_over:
                time.sleep(1)
                board.restart(WIN)


            if event.type == pygame.MOUSEBUTTONDOWN and not board.game_over and not board.turn == O:

                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // 100)
                clicked_col = int(mouseX // 100)
                if board.turn == X:
                    board.mark_square(WIN, clicked_row, clicked_col, X)
                print(board.board)
                board.drawing.draw_grid(WIN)
                board.drawing.draw_shape(WIN, board.board)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.restart(WIN)
                    board.game_over = False

        # board.draw_grid(WIN, board.turn, clicked_row, clicked_col)

        pygame.display.update()
        # print(board.game_over)



    pygame.quit()
    # board.restart(WIN)


if __name__ == '__main__':
    main()
