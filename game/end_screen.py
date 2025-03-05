import pygame, sys
from game.settings import *


# Splash Screen
def endScreen(surface, clock, score):
    font = pygame.font.Font("assets/font/font.otf", round(8 * SCREEN_SCALER))
    message = font.render(f"Game Over! Presents Delivered: {score}", True, (255, 255, 255))
    timer = 0
    duration = 5

    while timer < duration:
        # deltaTime
        deltaTime = clock.tick(FPS) / 1000
        timer += deltaTime

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear Screen
        surface.fill("black")

        # Display Message
        surface.blit(message, (WIDTH/2 - message.get_width()/2, HEIGHT/2 - message.get_height()/2))

        # Update Screen
        pygame.display.flip()
