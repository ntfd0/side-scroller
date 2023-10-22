import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
    """A class to represent a single drop of rain"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen

        # Load the raindrop image and set its rect attr
        self.image = pygame.image.load('img/raindrop.png')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen
        # (with an offset based on the drop's width and height)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the drop's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Fetch the settings
        self.settings = game.settings

    def check_edge(self):
        """Return True if raindrop reached the left side of the screen"""
        return (self.rect.topright[1] <= 0)