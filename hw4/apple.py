import pygame

class Apples:
    def __init__(self):
        self.apple_list = []

    def set_apple(self, Apple):
        self.apple_list.append(Apple)

    def draw(self, BOARD):
        # apple을 그린다.
        for i in self.apple_list:
            pygame.draw.circle(BOARD, i.color, i.pos, 15)


class Apple:
    def __init__(self, color, rgb, pos, length, direction, point, speed):
        self.color = color
        self.rgb = rgb
        self.pos = pos
        self.length = length
        self.direction = direction
        self.point = point
        self.speed = speed
