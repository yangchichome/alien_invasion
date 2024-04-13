import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen  # Get the screen surface from the game instance
        self.screen_rect = self.screen.get_rect()  # Get the rectangular area of the screen

        # Load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')  # Load the ship image
        self.rect = self.image.get_rect()  # Get the rectangle representing the image

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom  # Center the ship at the bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)  # Draw the image onto the screen at the specified rectangle
