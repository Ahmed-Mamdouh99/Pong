import pygame

WHITE = 255, 255, 255


class Paddle(object):
    def __init__(self, pos=[0,0], dimensions=(20,100), speed=5,
            up=pygame.K_UP, dwn=pygame.K_DOWN, direc=0):
        self.surface = pygame.Surface(dimensions)
        self.surface.fill(WHITE)
        self.rect = self.surface.get_rect().move(pos)
        self.up = up
        self.dwn = dwn
        self.speed = speed
        self.direc = direc


    def move(self, frect):
        if self.direc == 1 and self.rect.bottom + self.speed > frect.bottom:
            self.direc = 0
        elif self.direc == -1 and self.rect.top + self.speed < frect.top:
            self.direc = 0
        self.rect = self.rect.move([0, self.speed * self.direc])
