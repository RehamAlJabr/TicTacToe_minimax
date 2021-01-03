import pygame
from TicTacToe import WIDTH, HEIGHT
from TicTacToe.board import Board
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

board = Board()
FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    clicked_row = 0
    clicked_col = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = int(mouseY // 100)
                clicked_col = int(mouseX // 100)
                # print(clicked_row, clicked_col)
                board.mark_square(clicked_row, clicked_col, 1)
                print(board.board)
                board.draw_grid(WIN, 1, clicked_row, clicked_col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.restart(WIN)

        print(clicked_row, clicked_col)
        board.draw_grid(WIN, 1, clicked_row, clicked_col)
        pygame.display.update()



    pygame.quit()


if __name__ == '__main__':
    main()
