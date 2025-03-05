import pygame
import random
from game.settings import *
from game.sound_manager import play_sound, play_sound_from_folder

# Present Texture
present_texture = pygame.transform.scale_by(pygame.image.load("assets/gfx/present.png"), SCREEN_SCALER)

# Address Names
names = [
    "Mason",
    "Harper",
    "Liam",
    "Chloe",
    "Benjamin",
    "Scarlett",
    "Jackson",
    "Amelia",
    "Samuel",
    "Lily",
    "Aiden",
    "Grace",
    "Ethan",
    "Abigail",
    "Sebastian",
    "Mia",
    "Henry",
    "Olivia",
    "Elijah",
    "Ella"
]


# Present Class
class Present:
    def __init__(self, spawn, house_list):
        self.image = present_texture
        self.rect = self.image.get_rect()
        self.spawn = spawn

        self.isCarried = False
        self.house_list = house_list
        self.house = ""
        self.address = ""
        self.gift_tage_name = ""

    def reset(self):
        self.rect.center = self.spawn
        self.isCarried = False
        self.gift_tage_name = ""

    def pick_up(self):
        play_sound("pop.ogg")
        self.isCarried = True

        self.house = random.choice(self.house_list)
        self.address = self.house.name
        self.gift_tage_name = random.choice(names)

    def update(self, player):
        if not self.isCarried:
            # Check collision with player
            if self.rect.colliderect(player.hitBox):
                self.pick_up()
        else:
            # Check collision with house
            if player.hitBox.colliderect(pygame.Rect(self.house.x, self.house.y, self.house.width, self.house.height)):
                self.reset()
                play_sound_from_folder("ThankYou")
                return True
        return False
