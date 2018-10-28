import pygame

WHITE = 255, 255, 255


class Frame(object):
    def __init__(self, pos=[0,0], dimensions=(1360,768), width=1):
        self.surface = pygame.Surface(dimensions)
        pygame.draw.rect(self.surface, WHITE, [0, 0, dimensions[0], dimensions[1]], width)
        self.rect = self.surface.get_rect().move(pos)
        self.width = width
