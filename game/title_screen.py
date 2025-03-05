import pygame, sys
import os
from game.settings import *
from game.snow_animation import SnowAnimation


# Splash Screen
def titleScreen(surface, clock):
    title_screen_path = os.getcwd() + "/assets/gfx/ui/title_screen.png"
    title_screen = pygame.transform.scale_by(pygame.image.load(title_screen_path), SCREEN_SCALER)
    snow_animation = SnowAnimation()
    snow_animation.start()

    run = True
    while run:
        # deltaTime
        deltaTime = clock.tick(FPS) / 1000

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                run = False

        # Draw title_screen
        surface.blit(title_screen, (0, 0))

        # Draw Snow
        snow_animation.update(deltaTime)
        snow_animation.render()

        # Update Screen
        pygame.display.flip()
