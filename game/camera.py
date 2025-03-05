import pygame
from game.settings import *


# Camera Class
class Camera:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def update(self, target):
        self.offset.x = target.rect.centerx - WIDTH / 2
        self.offset.y = target.rect.centery - HEIGHT / 2

    def draw_group(self, group):
        for sprite in group:
            offset_pos = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_pos)

    def draw_object(self, obj):
        offset_pos = obj.rect.topleft - self.offset
        self.surface.blit(obj.image, offset_pos)

    def draw_hitBox(self, hitBox, color=(255, 0, 0)):
        offset_hitBox = hitBox.copy()
        offset_hitBox.topleft -= self.offset
        pygame.draw.rect(self.surface, color, offset_hitBox, 2)
