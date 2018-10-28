import pygame

GREEN = 0, 255, 0


class Scoreboard(object):
    def __init__(self, score, pos):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surface = self.font.render(str(score[0])+':'+str(score[1]), False, GREEN)
        self.rect = pos


    def update(self, score):
        self.surface = self.font.render(str(score[0])+':'+str(score[1]), False, GREEN)
