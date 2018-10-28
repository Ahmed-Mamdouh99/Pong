import pygame

GREEN = 0, 255, 0


class Pausetext(object):
    def __init__(self, text='PAUSED'):
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surface = self.font.render(text, False, GREEN)
