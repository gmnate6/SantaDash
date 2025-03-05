import pygame
import random
from game.settings import *

# Snow Texture
snow_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/particles/snow.png"), SCREEN_SCALER * .01)


# Snow Particle Class
class SnowParticle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale_by(snow_texture.copy(),  random.uniform(.5, 1.5))
        self.rect = self.image.get_rect()
        self.rect.center = (random.uniform(0, WIDTH), random.uniform(0, HEIGHT))

        # Movement
        self.velocity = pygame.math.Vector2(-random.uniform(75, 125), random.uniform(75, 125)) * SCREEN_SCALER
        self.random_factor = 100 * SCREEN_SCALER

    def update(self, deltaTime):
        # Movement
        displacement = self.velocity * deltaTime
        self.velocity += pygame.math.Vector2(random.uniform(-self.random_factor, self.random_factor), random.uniform(-self.random_factor, self.random_factor)) * deltaTime
        self.rect.center += displacement

        # Wrap around the screen
        if self.rect.center[0] < 0:
            self.rect.x = WIDTH
        if self.rect.center[1] > HEIGHT:
            self.rect.y = 0


# Snow Animation Class
class SnowAnimation:
    def __init__(self):
        self.running = False
        self.snow_list = pygame.sprite.Group()
        self.surface = pygame.display.get_surface()

    def start(self, num=50):
        if self.running:
            return

        # Setup
        self.running = True
        self.snow_list.empty()

        # Generate snow particles
        for _ in range(num):
            snow = SnowParticle()
            self.snow_list.add(snow)

    def stop(self):
        self.running = False

    def render(self):
        self.snow_list.draw(self.surface)

    def update(self, deltaTime):
        if self.running:
            # Update confetti positions
            self.snow_list.update(deltaTime)
