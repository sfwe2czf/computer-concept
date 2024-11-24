import pygame
from pygame.locals import QUIT

class Board:
    def __init__(self, stud_id, name):
        self.stud_id = stud_id
        self.name = name
        self._length = 0
        self._speed = 0
        self._score = 0
        self._highscore = 0
        self._time = 0

    # setter
    def set_length(self, length):
        self._length = length

    # getter
    def get_speed(self):
        return self._speed

    # setter
    def set_speed(self, speed):
        self._speed = speed

    # getter
    def get_score(self):
        return self._score

    # setter
    def set_score(self, score):
        self._score = score

    # getter
    def get_highest_score(self):
        return self._highscore

    # setter
    def set_highest_score(self, high_score):
        self._highscore = high_score

    # getter
    def get_time(self):
        return self._time

    # setter
    def set_time(self, time):
        self._time = time

    # draw board
    def draw(self, BOARD):
        """
        화면 상단에 학번, 이름을 나타내고 화면 우측에 점수, 최고점수, 길이, 속도, 시간을 나타낸다.
        화면 중앙에는 width=30, height=30인 25x25 격자를 그린다.
        """

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            BOARD.fill((0, 0, 0))
            font = pygame.font.SysFont("malgungothic", 30, True)
            scard = font.render(f"Student ID: {self.stud_id}", True, (0, 0, 255))
            namae = font.render(f"Name: {self.name}", True, (0, 255, 0))
            jumsoo = font.render(f"Score: {self._score}", True, (255, 0, 0))
            bestjumsoo = font.render(f"High score: {self._highscore}", True, (0, 255, 255))
            giri = font.render(f"Length: {self._length}", True, (255, 255, 0))
            sokdo = font.render(f"Speed: {self._speed}", True, (255, 0, 255))
            sigan = font.render(f"Time: {self._time}", True, (255, 255, 255))
            BOARD.blit(scard, [20, 5])
            BOARD.blit(namae, [600, 5])
            BOARD.blit(jumsoo, [775, 70])
            BOARD.blit(bestjumsoo, [775, 190])
            BOARD.blit(giri, [775, 310])
            BOARD.blit(sokdo, [775, 430])
            BOARD.blit(sigan, [775, 550])
            White = (255, 255, 255)
            for row in range(26):
                pygame.draw.line(BOARD, White, (20, 40+row*30), (770, 40+row*30))
            for col in range(26):
                pygame.draw.line(BOARD, White, (20 + col*30, 40), (20 + col*30, 790))

            # 작업한 BOARD의 내용을 갱신
            pygame.display.update()

    def game_over(self, file_dir, BOARD):
        """
        화면에 Game Over를 띄우고 highscore를 score.txt 파일에 저장한다.
        """
        font = pygame.font.SysFont(None, 200, True)
        over = font.render("Game Over", True, (255, 0, 0))
        BOARD.blit(over, [30, 400])
        f = open(file_dir, "w")
        f.write(f"{self._highscore}")
        f.close()

    # load highest score
    def load_highest_score(self, file_dir):
        """
        score.txt 파일로부터 highscore를 불러오며, 파일이 없거나 점수가 없을 경우 highscore는 0이다.
        """
        try:
            f = open(file_dir, "r")
            self._highscore = int(f.readline().strip())
            f.close()
        except IOError:
            self._highscore = 0


