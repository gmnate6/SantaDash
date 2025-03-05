import pygame, os
import random

songs = ["here_comes_santa.ogg", "merry_christmas.ogg", "sleigh_ride.ogg"]
sfx_path = "assets/sfx/"


def play_music():
    if pygame.mixer.music.get_busy():
        return

    full_path = sfx_path + "music/" + random.choice(songs)
    pygame.mixer.music.load(full_path)
    pygame.mixer.music.play()


def play_sound(file_name, volume=.4):
    full_path = sfx_path + file_name
    sound = pygame.mixer.Sound(full_path)
    sound.set_volume(volume)
    pygame.mixer.Sound.play(sound)


def play_sound_from_folder(folder_name, volume=.05):
    path = sfx_path + folder_name + "/"

    # Get number of sounds in folder
    count = 0
    for _, __, files in os.walk(path):
        count += len(files)

    file_name = folder_name + "/" + str(random.randrange(count) + 1) + ".ogg"
    play_sound(file_name, volume)

def pause_sounds():
    pygame.mixer.pause()

def unpause_sounds():
    pygame.mixer.unpause()
