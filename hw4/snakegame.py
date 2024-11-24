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


class SnakeGame:
    def __init__(self, stud_id, name, snake_pos):
        self.key = K_DOWN
        self.game_over = False

        self.apples = Apples()          #apples initialize
        self.snake = Snake(snake_pos)   #snake initialize
        self.board = Board(stud_id, name)    #board initialize


    def add_apple(self, snake, is_gold):
        # 각 색깔에 해당하는 확률에 맞게 Apple instance를 만들어서 Apples class에 넣기
        # add apple 하나씩
        Apples.set_apple(Apple("Green", (51, 204, 51), pos, 1, False, 1, 0))


    def init_apple(self, snake):
        # snake를 피해서 random 하게 apple initialize
        return -1

    def update_status(self, apple):
        # 먹은 사과의 역할에 맞게 status update
        return -1

    def paint(self):
        # 게임 화면 그리기
        return -1


    def do_game(self):

        """ implement  here """

        self.init_apple(self.snake)

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.key = event.key

            clock.tick(self.board.get_speed())
