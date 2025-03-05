import pygame
import random
from game.settings import *
from game.sound_manager import play_sound

# Confetti Texture
confetti_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/particles/confetti.png"), SCREEN_SCALER)


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# ConfettiParticle Class
class ConfettiParticle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = confetti_texture.copy()
        # Set color
        self.image.fill(get_random_color(), special_flags=pygame.BLEND_RGBA_MULT)
        # Set size
        self.image = pygame.transform.scale_by(self.image,  random.uniform(.1, .4))
        self.rect = self.image.get_rect(center=pos)

        self.velocity = pygame.math.Vector2(random.uniform(-25, 25), -random.uniform(30, 50)) * SCREEN_SCALER
        self.acceleration = pygame.math.Vector2(0, random.uniform(50, 70)) * SCREEN_SCALER
        self.drag_acceleration = 7 * SCREEN_SCALER

    def update(self, deltaTime):
        # Movement
        displacement = self.velocity * deltaTime + (.5 * self.acceleration * deltaTime ** 2)
        self.velocity += self.acceleration * deltaTime
        self.rect.center += displacement

        # Apply Drag in opposite direction of velocity
        drag = self.drag_acceleration * deltaTime
        if self.velocity.x > 0:
            self.velocity.x = max(0, self.velocity.x - drag)
        elif self.velocity.x < 0:
            self.velocity.x = min(0, self.velocity.x + drag)


# ConfettiAnimation Class
class ConfettiAnimation:
    def __init__(self):
        self.running = False
        self.confetti_list = pygame.sprite.Group()
        self.timer = 0

    def start_confetti(self, pos, num_confetti=50):
        if self.running:
            return

        # Setup
        self.running = True
        self.confetti_list.empty()  # Clear existing confetti particles
        self.timer = 0

        # Generate confetti particles at a specific position
        for _ in range(num_confetti):
            confetti = ConfettiParticle(pos)
            self.confetti_list.add(confetti)

        # Play sound
        play_sound("confetti.ogg", volume=.05)

    def update(self, deltaTime):
        if self.running:
            # Update confetti positions
            self.confetti_list.update(deltaTime)

            # Update timer
            self.timer += deltaTime

            # If time is up
            if self.timer > 1.5:
                self.stop_confetti()

    def stop_confetti(self):
        self.running = False
