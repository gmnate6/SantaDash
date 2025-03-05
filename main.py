import pygame, sys
from game.settings import *
from game.splash_screen import splashScreen
from game.title_screen import titleScreen
from game.sound_manager import play_music
from game.level import Level
from game.end_screen import endScreen


# Pygame Setup
pygame.init()
pygame.display.set_caption("Santa's Present Dash!")
pygame.display.set_icon(pygame.image.load("assets/gfx/ui/icon.png"))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


# Main Code
if __name__ == "__main__":
    # Splash Screen
    splashScreen(screen, clock)

    # Game Loop
    while True:
        # Title Screen
        play_music()
        titleScreen(screen, clock)

        # Load Level
        level = Level(screen)

        # Level Loop
        clock.tick(FPS)
        run = True
        while run:
            # deltaTime
            deltaTime = clock.tick(FPS) / 1000

            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Clear Screen
            screen.fill("black")

            # Run Level
            run = level.run(deltaTime)

            # Play music
            play_music()

            # Update Screen
            pygame.display.flip()

        # End Screen
        endScreen(screen, clock, level.ui.score)
