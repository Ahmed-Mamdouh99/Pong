import pygame

WHITE = 255, 255, 255


class Ball(object):
    def __init__(self, pos=[0, 0], radius=10, speed=[4,4]):
        self.surface = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(self.surface, WHITE, [radius, radius], radius)
        self.rect = self.surface.get_rect().move(pos)
        self.speed = speed


    def move(self):
        self.rect = self.rect.move(self.speed)
