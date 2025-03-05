import pygame
from game.settings import *


# UI Class
class UI:
    def __init__(self):
        self.get_assets()

        self.surface = pygame.display.get_surface()
        self.image = self.overLay_texture
        self.rect = self.image.get_rect()

        self.score = 0
        self.timer = 60
        self.present_address = ""

    def get_assets(self):
        # Textures
        self.overLay_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/ui/over_lay.png"), SCREEN_SCALER)
        self.giftTag_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/ui/gift_tag.png"), SCREEN_SCALER)
        self.icon_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/ui/icon.png"), SCREEN_SCALER)

        # Font
        self.font_12 = pygame.font.Font("assets/font/font.otf", round(12 * SCREEN_SCALER))
        self.font_10 = pygame.font.Font("assets/font/font.otf", round(10 * SCREEN_SCALER))

    def update(self, deltaTime, present_address):
        # Update Timer
        self.timer -= deltaTime
        if self.timer < 0:
            self.timer = 0

        # Update Present Address
        self.present_address = present_address

    def draw(self):
        # Get texts
        timer_message = self.font_12.render(f"Timer: {round(self.timer, 2)}", True, (255, 255, 255))
        get_gift_message = self.font_10.render("Get Gift!", True, (255, 255, 255))
        gift_tage_message = self.font_10.render(f"To: {self.present_address}", True, (0, 0, 0))
        score_message = self.font_10.render(f"Score: {self.score}", True, (255, 255, 255))

        # Draw
        self.surface.blit(self.image, self.rect)
        self.surface.blit(timer_message, (SCREEN_SCALER, SCREEN_SCALER))
        self.surface.blit(score_message, (WIDTH - 40 * SCREEN_SCALER, score_message.get_height()/4))
        if self.present_address != "":
            self.surface.blit(self.giftTag_texture, (WIDTH/2 - self.giftTag_texture.get_width()/2, 0))
            self.surface.blit(gift_tage_message, (WIDTH/2 - 10 * SCREEN_SCALER, 3 * SCREEN_SCALER))
        else:
            self.surface.blit(get_gift_message, (WIDTH / 2 - get_gift_message.get_width()/2, 3 * SCREEN_SCALER))
