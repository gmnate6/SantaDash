import pygame, sys
from game.settings import *


# Splash Screen
def splashScreen(surface, clock):
    font = pygame.font.Font("assets/font/font.otf", round(8 * SCREEN_SCALER))
    startMessage = font.render("CREATED BY NATHAN", True, (255, 255, 255))
    timer = 0
    duration = 2

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
        surface.blit(startMessage, (WIDTH/2 - startMessage.get_width()/2, HEIGHT/2 - startMessage.get_height()/2))

        # Update Screen
        pygame.display.flip()
