import pygame
import math
from game.settings import *

# Arrow Texture
arrow_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/ui/arrow.png"), SCREEN_SCALER)


# Arrow Class
class Arrow:
    def __init__(self):
        self.image = arrow_texture
        self.rect = self.image.get_rect()
        self.active = False
        self.visible = True
        self.angle = 0
        self.offset = pygame.math.Vector2(0, -10) * SCREEN_SCALER
        self.min_distance = 16 * SCREEN_SCALER

    def update(self, player, target=pygame.math.Vector2()):
        # Returns if not active
        if not self.active:
            return

        # Calculate angle
        x = target.x - player.hitBox.x
        y = target.y - player.hitBox.y
        self.angle = math.degrees(math.atan2(-y, x))

        # Rotate the arrow image
        self.image = pygame.transform.rotate(arrow_texture, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Set the arrow pos
        self.rect.center = player.rect.center + self.offset

        # Turn off Arrow if to close to target
        if pygame.math.Vector2(x, y).length() < self.min_distance:
            self.visible = False
        else:
            self.visible = True
