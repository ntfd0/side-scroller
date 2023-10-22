import pygame

class Bullet(pygame.sprite.Sprite):
    """A class that creates bullets"""
    def __init__(self, game):
        """Create a bullet object fired by the character"""
        super().__init__()
        self.settings = game.settings
        
        self.screen = game.screen
        self.color = self.settings.BULLET_COLOR

        # Create a bullet rect at 0,0, then set correct position
        self.rect = pygame.Rect(0, 0, 
                                self.settings.BULLET_WIDTH, 
                                self.settings.BULLET_HEIGHT)
        self.rect.midleft = game.char.rect.midright

        # Store the bullet's position as float
        self.x = float(self.rect.x)

    def update(self):
        """Update the bullet's position"""
        self.x += self.settings.BULLET_SPEED
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet_Counter:
    """A classs that shows UI text with number of bullets"""
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # Initiatie the counter
        self.counter = self.settings.MAX_BULLETS
        # Choose a font and size
        self.font = pygame.font.SysFont(None, 
                                        game.settings.COUNTER_FONT_SIZE)
        # Update & blit the text
        self.update_text()

    def update_text(self):
        """Update the text & blit it"""
        text = self.font.render(f'Bullets: {self.counter}/{self.settings.MAX_BULLETS}', 
                                True,
                                self.settings.BACKGROUND_COLOR, 
                                self.settings.TEXT_COLOR)
        # Position the text at the top right corner
        rect = text.get_rect()
        rect.topright = self.screen_rect.topright
        # Blit
        self.screen.blit(text, rect)