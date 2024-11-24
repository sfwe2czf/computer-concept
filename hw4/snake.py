import pygame
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

class Snake:
    def __init__(self, snake_pos, direction=0):
        self.bodies = [snake_pos]
        self.len = len(self.bodies)

    def move(self, key, apples="Green"):
        # move snake, game over 여부를 판정한다.
        # return is_game_over
        if key == pygame.K_LEFT and (self.len == 1 or not(self.bodies[0][0] == self.bodies[1][0]+30 and self.bodies[0][1] == self.bodies[1][1])):
            new_list = []
            new_list.append(self.bodies[0][0]-30)
            for i in range(1, len(self.bodies)):
                new_list.append(self.bodies[i-1])
            self.bodies = new_list
        if key == pygame.K_RIGHT and (self.len == 1 or not(self.bodies[0][0] == self.bodies[1][0]-30 and self.bodies[0][1] == self.bodies[1][1])):
            new_list = []
            new_list.append(self.bodies[0][0] + 30)
            for i in range(1, len(self.bodies)):
                new_list.append(self.bodies[i - 1])
            self.bodies = new_list
        if key == pygame.K_UP and (self.len == 1 or not(self.bodies[0][0] == self.bodies[1][0] and self.bodies[0][1] == self.bodies[1][1]+30)):
            new_list = []
            new_list.append(self.bodies[0][1] - 30)
            for i in range(1, len(self.bodies)):
                new_list.append(self.bodies[i - 1])
            self.bodies = new_list
        if key == pygame.K_DOWN and (self.len == 1 or not(self.bodies[0][0] == self.bodies[1][0] and self.bodies[0][1] == self.bodies[1][1]-30)):
            new_list = []
            new_list.append(self.bodies[0][1] + 30)
            for i in range(1, len(self.bodies)):
                new_list.append(self.bodies[i - 1])
            self.bodies = new_list

        if self.bodies[0][0] < 20 or self.bodies[0][0] >= 770 or self.bodies[0][1] < 40 or self.bodies[0][1] >= 790 or (self.bodies[0] in (self.bodies[n] for n in range(1, len(self.bodies)))):
            return False


    def draw(self, BOARD):
        # snake을 그린다.
        # rgb code는 head의 경우, (51, 153, 255), 몸통의 경우 (0, 255, 255)을 이용한다.
        for i in self.bodies:
            if i == self.bodies[0]:
                pygame.draw.rect(BOARD, (51, 153, 255), (i[0], i[1], 30, 30))
            else:
                pygame.draw.rect(BOARD, (0, 255, 255), (i[0], i[1], 30, 30))
    def change_direction(self):
        # change snake's direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.move(pygame.K_UP)
                elif event.key == pygame.K_DOWN:
                    self.move(pygame.K_DOWN)
                elif event.key == pygame.K_LEFT:
                    self.move(pygame.K_LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.move(pygame.K_RIGHT)

