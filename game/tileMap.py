import pygame
from game.settings import *
from pytmx.util_pygame import load_pygame


# Tile Class
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, texture, collision):
        super().__init__()
        self.image = pygame.transform.scale_by(texture, SCREEN_SCALER)
        self.rect = self.image.get_rect(topleft=pos)
        self.collision = collision

    def update(self, shift):
        return
        self.rect.x -= shift.x
        self.rect.y -= shift.y


# TileMap Class
class TileMap:
    def __init__(self, path):
        self.path = path
        self.tileMap = load_pygame(path)

    def get_tileMap(self):
        tiles = pygame.sprite.Group()

        # For each layer
        for layer in self.tileMap.visible_layers:
            # For each tile
            for x_index, y_index, surf in layer.tiles():
                # Pos on Screen
                x = x_index * TILE_SIZE * SCREEN_SCALER
                y = y_index * TILE_SIZE * SCREEN_SCALER
                # Add Tile
                tiles.add(Tile((x, y), surf, layer.properties["collisionBool"]))
        # Return
        return tiles

    def get_tileMap_objects(self):
        result = {}
        for obj_group in self.tileMap.objectgroups:
            for obj in obj_group:
                # Apply SCREEN_SCALE to obj.pos
                obj.x *= SCREEN_SCALER
                obj.y *= SCREEN_SCALER

                # Apply SCREEN_SCALE to obj.pos
                obj.width *= SCREEN_SCALER
                obj.height *= SCREEN_SCALER

                result[obj.name] = obj
        return result
