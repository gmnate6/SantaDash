import pygame
import os
from game.settings import *


def import_texture_folder(path):
    surface_list = []
    for _, __, img_file_list in os.walk(path):
        for img_file in img_file_list:
            full_path = path + "/" + img_file
            surface = pygame.transform.scale_by(pygame.image.load(full_path), SCREEN_SCALER)
            surface_list.append(surface)

    return surface_list


def import_texture_assets(path, file_name_list):
    assets = {}

    for file_name in file_name_list:
        full_path = path + file_name
        assets[file_name] = import_texture_folder(full_path)

    return assets
