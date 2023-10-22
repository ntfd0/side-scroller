import pygame

class Character:
    """A class that creates a character"""
    def __init__(self, game):
        self.settings = game.settings

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('img/fanteria.gif').convert()
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Method for bliting"""
        self.update()
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Method to update the character's location based on keys pressed"""
        if self.moving_up == True and self.rect.top > 0:
            self.y -= self.settings.CHAR_SPEED
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.CHAR_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

 