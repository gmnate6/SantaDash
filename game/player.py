import pygame
from game.settings import *
from game.import_assets import import_texture_assets
from game.sound_manager import play_sound_from_folder


class Player:
    def __init__(self, pos):
        # Sprite
        self.frame_index = 0
        self.import_texture_assets()
        self.status = "walk_down"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos

        # Movement Constants
        self.movement_top_speed = 100 * SCREEN_SCALER
        self.movement_acceleration = 200 * SCREEN_SCALER
        self.drag_factor = .7

        # Movement Vectors
        self.velocity = pygame.math.Vector2()
        self.acceleration = pygame.math.Vector2()

        # HitBox Rect
        self.hitBox_dx = 3
        self.hitBox_dy = 22
        self.hitBox_Height = 10
        self.hitBox_Width = 10
        hitBox_x = self.rect.x + self.hitBox_dx * SCREEN_SCALER
        hitBox_y = self.rect.y + self.hitBox_dy * SCREEN_SCALER
        hitBox_width = self.hitBox_Width * SCREEN_SCALER
        hitBox_height = self.hitBox_Height * SCREEN_SCALER
        self.hitBox = pygame.Rect(hitBox_x, hitBox_y, hitBox_width, hitBox_height)

    def handle_input(self):
        # Get Keys
        keys = pygame.key.get_pressed()

        # Determine the direction based on keys pressed
        x_direction = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y_direction = keys[pygame.K_DOWN] - keys[pygame.K_UP]

        # Normalize the acceleration vector
        acceleration_magnitude = pygame.math.Vector2(x_direction, y_direction).length()
        if acceleration_magnitude > 0:
            self.acceleration = pygame.math.Vector2(x_direction, y_direction) * self.movement_acceleration / acceleration_magnitude
        else:
            self.acceleration = pygame.math.Vector2(0, 0)

        # If no keys are being pressed: Reset Acceleration
        if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.acceleration.y = 0
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.acceleration.x = 0

    def apply_drag(self, deltaTime):
        drag = self.drag_factor * self.movement_acceleration * deltaTime

        # Apply Drag in opposite direction of velocity
        if self.acceleration.x == 0:
            if self.velocity.x > 0:
                self.velocity.x = max(0, self.velocity.x - drag)
            elif self.velocity.x < 0:
                self.velocity.x = min(0, self.velocity.x + drag)

        if self.acceleration.y == 0:
            if self.velocity.y > 0:
                self.velocity.y = max(0, self.velocity.y - drag)
            elif self.velocity.y < 0:
                self.velocity.y = min(0, self.velocity.y + drag)

    def update_movement_x(self, deltaTime):
        displacement_x = self.velocity.x * deltaTime + (.5 * self.acceleration.x * deltaTime ** 2)
        self.velocity.x += self.acceleration.x * deltaTime
        self.rect.x += displacement_x
        # Update hitBox
        self.hitBox_to_player()

    def update_movement_y(self, deltaTime):
        displacement_y = self.velocity.y * deltaTime + (.5 * self.acceleration.y * deltaTime ** 2)
        self.velocity.y += self.acceleration.y * deltaTime
        self.rect.y += displacement_y
        # Update hitBox
        self.hitBox_to_player()

    def normalize_movement(self):
        # Cap Speed
        if self.velocity.length() > self.movement_top_speed:
            self.velocity.scale_to_length(self.movement_top_speed)

    def hitBox_to_player(self):
        # Move hitBox to player
        hitBox_x = self.rect.x + self.hitBox_dx * SCREEN_SCALER
        hitBox_y = self.rect.y + self.hitBox_dy * SCREEN_SCALER
        self.hitBox.topleft = (hitBox_x, hitBox_y)

    def player_to_hitBox(self):
        # Move player to hitBox
        player_x = self.hitBox.x - self.hitBox_dx * SCREEN_SCALER
        player_y = self.hitBox.y - self.hitBox_dy * SCREEN_SCALER
        self.rect.topleft = (player_x, player_y)

    def import_texture_assets(self):
        path = "assets/gfx/santa/"
        file_name_list = ["walk_up", "walk_down", "walk_right", "walk_left"]
        self.animations = import_texture_assets(path, file_name_list)

    def get_status(self):
        # Get Keys
        keys = pygame.key.get_pressed()

        # Up
        if keys[pygame.K_UP]:
            # Check if down key is not pressed
            if not keys[pygame.K_DOWN]:
                # Animation
                self.status = "walk_up"
            else:
                # Reset animation
                self.frame_index = 0
                self.animate()
                self.status = ""
        # Down
        elif keys[pygame.K_DOWN]:
            # Check if up key is not pressed
            if not keys[pygame.K_UP]:
                # Animation
                self.status = "walk_down"
            else:
                # Reset animation
                self.frame_index = 0
                self.animate()
                self.status = ""
        # Right
        elif keys[pygame.K_RIGHT]:
            # Check if left key is not pressed
            if not keys[pygame.K_LEFT]:
                # Animation
                self.status = "walk_right"
            else:
                # Reset animation
                self.frame_index = 0
                self.animate()
                self.status = ""
        # Left
        elif keys[pygame.K_LEFT]:
            # Check if right key is not pressed
            if not keys[pygame.K_RIGHT]:
                # Animation
                self.status = "walk_left"
            else:
                # Reset animation
                self.frame_index = 0
                self.animate()
                self.status = ""
        else:
            # Reset animation
            self.frame_index = 0
            self.animate()
            self.status = ""

    def animate(self):
        # Return if no animation
        if self.status == "":
            return

        # Default Settings
        repeat = True
        delay = 0
        speed = .2
        if self.status == "":
            speed = 0
        elif self.status == "walk_up":
            pass
        elif self.status == "walk_down":
            pass
        elif self.status == "walk_right":
            pass
        elif self.status == "walk_left":
            pass

        # Get animation
        animation = self.animations[self.status]

        # Loop over frame index
        self.frame_index += speed
        if repeat:
            if self.frame_index >= len(animation)+delay:
                self.frame_index = 0

        # Set Image
        self.image = animation[min(int(self.frame_index), len(animation) - 1)]

    def play_player_sounds(self):
        # Walk Sound
        if self.status in ["walk_up", "walk_down", "walk_right", "walk_left"]:
            if self.frame_index == 1:
                play_sound_from_folder("SnowWalk")

    def update(self, deltaTime):
        # Input/Movement
        self.handle_input()

        # Apply Drag
        self.apply_drag(deltaTime)

        # Animation
        self.get_status()
        self.animate()
        # Sounds
        self.play_player_sounds()
