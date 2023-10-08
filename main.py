import pygame
import sys

# Settings constants
GAME_TITLE = 'Fanteria'
CHAR_SPEED = 2.5
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BULLET_SPEED = 10
BULLET_COLOR = (75, 0, 130)
BULLET_WIDTH = 15
BULLET_HEIGHT = 3
MAX_BULLETS = 5

TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 255)

COUNTER_FONT_SIZE = 55

class Bullet(pygame.sprite.Sprite):
    """A class that creates bullets"""
    def __init__(self, game):
        """Create a bullet object fired by the character"""
        super().__init__()
        self.screen = game.screen
        self.color = BULLET_COLOR

        # Create a bullet rect at 0,0, then set correct position
        self.rect = pygame.Rect(0, 0, 
                                BULLET_WIDTH, BULLET_HEIGHT)
        self.rect.midleft = game.char.rect.midright

        # Store the bullet's position as float
        self.x = float(self.rect.x)

    def update(self):
        """Update the bullet's position"""
        self.x += BULLET_SPEED
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet_Counter:
    """A classs that shows UI text with number of bullets"""
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        # Initiatie the counter
        self.counter = MAX_BULLETS
        # Choose a font and size
        self.font = pygame.font.SysFont(None, COUNTER_FONT_SIZE)
        # Update & blit the text
        self.update_text()

    def update_text(self):
        """Update the text & blit it"""
        text = self.font.render(f'Bullets: {self.counter}', True,
                           BACKGROUND_COLOR, TEXT_COLOR)
        # Position the text at the bottom right corner
        rect = text.get_rect()
        rect.bottomright = self.screen_rect.bottomright
        # Blit
        self.screen.blit(text, rect)


class Character:
    """A class that creates a character"""
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('fanteria.gif').convert()
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
            self.y -= CHAR_SPEED
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += CHAR_SPEED

        self.rect.x = self.x
        self.rect.y = self.y


class MainGame:
    def __init__(self):
        """Initiating the game"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)   
        # Make the char
        self.char = Character(self)
        # Initiate the Bullet group
        self.bullets = pygame.sprite.Group()
        self.bullet_counter = Bullet_Counter(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Check for any mouse/keyboard events
            self._check_events()
            # Update the character
            self.char.update()
            # Update the bullets
            self._update_bullets()
            # Update the screen
            self._update_screen()
            # Set the clock (framerate) to 60 fps
            self.clock.tick(60)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill((220, 220, 220))
        # Blit the char
        self.char.blitme()
        # Redraw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Update the bullet counter
        self.bullet_counter.update_text()
        # Make the most recently drawn screen visible
        pygame.display.flip()
        
    def _check_events(self):
        """Respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            if event.type == pygame.KEYUP:
                self._check_events_keyup(event)

    def _check_events_keydown(self, event):
        """Helper method to process keydown events"""
        if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
            # Move the character up
             self.char.moving_up = True
        elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
            # Move the character down
             self.char.moving_down = True
        elif event.key == pygame.K_SPACE:
            # Fire bullets on spacebar
            self._fire_bullet()
        elif (event.key == pygame.K_q) or (event.key == pygame.K_ESCAPE):
            # If player presses Q or Escape, quit the game
            sys.exit()

    def _update_bullets(self):
        """Update the position of all bullets and remove old ones"""
        self.bullets.update()

        # Remove the ones that are outside of bounds
        for bullet in self.bullets.copy():
            if bullet.rect.right >= SCREEN_WIDTH:
                self.bullets.remove(bullet)
                self.bullet_counter.counter = MAX_BULLETS - len(self.bullets)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet sprite group"""
        if len(self.bullets) < MAX_BULLETS:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # Bullet counter updated depending on how many bullets have been fired
            self.bullet_counter.counter = MAX_BULLETS - len(self.bullets)

    def _check_events_keyup(self, event):
        """Helper method to process keyup events"""
        if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
            # Move the ship to the right
            self.char.moving_right = False
        elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
            # Move the ship to the left
             self.char.moving_left = False
        elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
            # Move the ship to the left
             self.char.moving_up = False
        elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
            # Move the ship to the left
             self.char.moving_down = False
        
            
if __name__ == '__main__':
    # Instantiate the game and run it
    rocket_game = MainGame()
    rocket_game.run_game()