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

class AI(SnakeGame):
    APPLE_INFO = None

    def __init__(self, stud_id, name, snake_pos, time_limit, n_apple):
        super().__init__(stud_id, name, snake_pos)

        self.time_limit = time_limit
        self.n_apple = n_apple
        self.movement = []

    def load_apple_info(self, file_dir):
        # apple.csv 파일에서 apple에 대한 정보를 읽어 class 변수 APPLE_INFO에 저장
        pass

    def get_movement(self):
        # self.movement에 움직일 방향을 저장
        pass

    def do_game(self):
        self.init_apple(self.snake)

        start_ticks = pygame.time.get_ticks()
        self.get_movement()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        if seconds <= 60:
            """ implement  here """
            while True:
                for event in self.movement:
                    pass

                clock.tick(self.board.get_speed())
        else:
            pygame.quit()
            sys.exit()