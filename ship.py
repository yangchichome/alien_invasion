import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen  # Get the screen surface from the game instance
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()  # Get the rectangular area of the screen

        # Load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')  # Load the ship image
        self.rect = self.image.get_rect()  # Get the rectangle representing the image

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # Center the ship at the bottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)  # Draw the image onto the screen at the specified rectangle

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # print("x ori", self.rect.x)
            self.x += self.settings.ship_speed
            # print("self.settings.ship_speed", self.settings.ship_speed)
            # print("x +", self.rect.x)
        if self.moving_left and self.rect.left > 0:
            # print("x ori", self.rect.x)
            self.x -= self.settings.ship_speed
            # print("self.settings.ship_speed", self.settings.ship_speed)
            # print("x -", self.rect.x)
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)