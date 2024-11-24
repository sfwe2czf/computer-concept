from snakegame import SnakeGame
from board import Board
from apple import *
from snake import Snake
import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

WIDTH = 1000
HEIGHT = 850
# pygame 초기화
pygame.init()
# BOARD 객체 저장
BOARD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

pygame.key.set_repeat(5, 5)

class UI(SnakeGame):
    APPLE_INFO = None

    def __init__(self, stud_id, name, snake_pos):
        super().__init__(stud_id, name, snake_pos)
        self.stud_id = stud_id
        self.name = name
    def load_apple_info(self, file_dir):
        # apple.csv 파일에서 apple에 대한 정보를 읽어 class 변수 APPLE_INFO에 저장
        pass

    def do_game(self):
        """ implement  here """
        Board(self.stud_id, self.name).draw(BOARD)
        snake = Snake([470, 160])
        snake.draw(BOARD)
        snake.change_direction()
        self.init_apple(self.snake)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.key = event.key

            clock.tick(self.board.get_speed())
