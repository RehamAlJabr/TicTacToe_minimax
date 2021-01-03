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
    clicked_row = 0
    clicked_col = 0
    board = Board()
    WIN.fill(WHITE)
    board.draw_grid(WIN)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            print(board.game_over)

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // 100)
                clicked_col = int(mouseX // 100)

                board.mark_square(WIN, clicked_row, clicked_col, board.turn)

                print(board.board)
                board.draw_grid(WIN)
                board.draw_shape(WIN, board.turn, clicked_row, clicked_col)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    board.restart(WIN)

        # board.draw_grid(WIN, board.turn, clicked_row, clicked_col)

        pygame.display.update()


        if board.game_over:

           board.restart(WIN)
           board.game_over = False




    pygame.quit()
    # board.restart(WIN)


if __name__ == '__main__':
    main()
