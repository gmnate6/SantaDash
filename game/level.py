import pygame
from game.settings import *
from game.tileMap import TileMap
from game.player import Player
from game.arrow import Arrow
from game.present import Present
from game.confetti_animation import ConfettiAnimation
from game.snow_animation import SnowAnimation
from game.ui import UI
from game.camera import Camera


# Level Class
class Level:
    def __init__(self, surface):
        self.surface = surface
        self.camera = Camera()
        self.setupLevel()

    def setupLevel(self):
        # Level Settings
        self.collisionBool = True
        self.showHitBoxes = False

        # TileMap Setup
        tileMap = TileMap("assets/tileMaps/level.tmx")
        self.tiles = tileMap.get_tileMap()
        # TileMap Objects
        self.tileMap_objects = tileMap.get_tileMap_objects()
        # Set Spawn
        spawn = self.tileMap_objects["spawn"]
        self.spawnPos = pygame.math.Vector2(spawn.x, spawn.y)

        # Player Setup
        self.player = Player(self.spawnPos)

        # Arrow Setup
        self.arrow = Arrow()
        self.arrow.active = True

        # Present Setup
        house_list = []
        for obj in self.tileMap_objects.values():
            if obj.properties["function"] == "house":
                house_list.append(obj)
        # Get Present_Spawn
        present_spawn_obj = self.tileMap_objects["present_spawn"]
        present_spawn_pos = pygame.math.Vector2(present_spawn_obj.x, present_spawn_obj.y)
        self.present = Present(present_spawn_pos, house_list)
        self.present.reset()

        # Confetti Setup
        self.confetti_animation = ConfettiAnimation()

        # Snow Setup
        self.snow_animation = SnowAnimation()
        self.snow_animation.start()

        # UI Setup
        self.ui = UI()

    def movement_collision(self, deltaTime):
        player = self.player

        # Update movement.x
        player.update_movement_x(deltaTime)
        # Check for collision
        if self.collisionBool:
            for tile in self.tiles.sprites():
                # Check if tile has collision
                if tile.collision:
                    # Check for collision with hitBox
                    if tile.rect.colliderect(player.hitBox):
                        if player.velocity.x > 0:  # Moving Right
                            player.hitBox.right = tile.rect.left
                        elif player.velocity.x < 0:  # Moving Left
                            player.hitBox.left = tile.rect.right
                        # Reset Velocity/Acceleration
                        player.velocity.x = 0
                        player.acceleration.x = 0
                        # Move player to hitBox
                        player.player_to_hitBox()
        # Update movement.y
        player.update_movement_y(deltaTime)
        # Check for collision
        if self.collisionBool:
            for tile in self.tiles.sprites():
                # Check if tile has collision
                if tile.collision:
                    # Check for collision with hitBox
                    if tile.rect.colliderect(player.hitBox):
                        if player.velocity.y > 0:  # Moving Down
                            player.hitBox.bottom = tile.rect.top
                        elif player.velocity.y < 0:  # Moving Up
                            player.hitBox.top = tile.rect.bottom
                        # Reset Velocity/Acceleration
                        player.velocity.y = 0
                        player.acceleration.y = 0
                        # Move player to hitBox
                        player.player_to_hitBox()

        # Normalize Movement
        player.normalize_movement()

    def draw_level(self):
        # Update Camera
        self.camera.update(self.player)

        # Draw Tiles
        self.camera.draw_group(self.tiles)

        # Draw Present
        if not self.present.isCarried:
            self.camera.draw_object(self.present)

        # Draw Player
        self.camera.draw_object(self.player)

        # Draw Arrow
        if self.arrow.visible:
            self.camera.draw_object(self.arrow)

        # Draw Confetti Animation
        if self.confetti_animation.running:
            self.camera.draw_group(self.confetti_animation.confetti_list)

        # Draw Snow Animation
        if self.snow_animation.running:
            self.snow_animation.render()

        # Draw HitBoxs
        if self.showHitBoxes:
            # Player HitBox
            self.camera.draw_hitBox(self.player.hitBox, color=(0, 0, 255))
            # Tiles HitBox
            for tile in self.tiles.sprites():
                if tile.collision:
                    self.camera.draw_hitBox(tile.rect)
            # Present HitBox
            if not self.present.isCarried:
                self.camera.draw_hitBox(self.present.rect, color=(0, 0, 255))
            # House HitBox
            for house in self.present.house_list:
                self.camera.draw_hitBox(pygame.Rect(house.x, house.y, house.width, house.height), color=(0, 255, 0))

        # Draw UI
        self.ui.draw()

    def run(self, deltaTime):
        # Update Player
        self.player.update(deltaTime)
        # Update Player Movement With Collision
        self.movement_collision(deltaTime)

        # Update Present
        if self.present.update(self.player):
            # Confetti
            x = self.present.house.x + self.present.house.width/2
            y = self.present.house.y + self.present.house.height/2 - 16 * SCREEN_SCALER
            self.confetti_animation.start_confetti((x, y))

            # Update Score
            self.ui.score += 1

        # Update Confetti Animation
        self.confetti_animation.update(deltaTime)

        # Update Snow Animation
        self.snow_animation.update(deltaTime)

        # Update Arrow
        if self.present.isCarried:
            self.arrow.update(self.player, self.present.house)
        else:
            self.arrow.update(self.player, self.present.rect)

        # Update UI
        self.ui.update(deltaTime, self.present.gift_tage_name)

        # Draw Level
        self.draw_level()

        # Return
        if self.ui.timer == 0:
            return False
        else:
            return True
