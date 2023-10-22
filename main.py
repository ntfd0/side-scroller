import pygame
import sys
from settings import Settings
from bullet import Bullet, Bullet_Counter
from character import Character
from raindrop import RainDrop
from random import randint

       
class MainGame:
    def __init__(self):
        """Initiating the game"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        pygame.display.set_caption(self.settings.GAME_TITLE)   
        # Make the char
        self.char = Character(self)
        # Initiate the Bullet group
        self.bullets = pygame.sprite.Group()
        # Create the bullet counter
        self.bullet_counter = Bullet_Counter(self)
        # Make a group for raindrops
        self.raindrops = pygame.sprite.Group()
        # Initiate a rain
        self._create_rain()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Check for any mouse/keyboard events
            self._check_events()
            # Update the character
            self.char.update()
            # Update the bullets
            self._update_bullets()
            # Update the raindrops
            self._update_raindrops()
            # Update the screen
            self._update_screen()
            # Set the clock (framerate) to 60 fps
            self.clock.tick(60)

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.GAME_BACKGROUND_COLOR)
        # Blit the char
        self.char.blitme()
        # Redraw the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Update the bullet counter
        self.bullet_counter.update_text()
        # Draw the aliens
        self.raindrops.draw(self.screen)
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
            if bullet.rect.right >= self.settings.SCREEN_WIDTH:
                self.bullets.remove(bullet)
                self.bullet_counter.counter = self.settings.MAX_BULLETS - len(self.bullets)
        self._check_bullet_raindrop_collisions()

    def _check_bullet_raindrop_collisions(self):
        """Respond to raindrop-bullet collision"""
        # Remove any bullets and raindrops that have collided
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.raindrops, True, True)
        # Check if there are any raindrops left
        if not self.raindrops:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_rain()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet sprite group"""
        if len(self.bullets) < self.settings.MAX_BULLETS:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # Bullet counter updated depending on how many bullets have been fired
            self.bullet_counter.counter = self.settings.MAX_BULLETS - len(self.bullets)

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

    def _create_rain(self):
        """Create a rain of raindrops"""
        
        for i in range(1,self.settings.MAX_RAINDROPS + 1):
            self._create_raindrop()

    def _create_raindrop(self):
        """Create a raindrop and place it randomly"""
        new_raindrop = RainDrop(self)
        new_raindrop.x = randint(self.settings.RAINDROP_START_X,
                                 self.settings.RAINDROP_END_X)
        new_raindrop.rect.x = new_raindrop.x
        new_raindrop.y = randint(self.settings.RAINDROP_START_Y,
                                 self.settings.RAINDROP_END_Y)
        new_raindrop.rect.y = new_raindrop.y
        self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        """Update the positions of all raindrops in the rain"""
        self._drop_raindrops()

    def _drop_raindrops(self):
        """Drop the entire rain"""
        for drop in self.raindrops.sprites():
            if drop.check_edge():
                self.raindrops.remove(drop)
            else:
                drop.rect.x -= self.settings.RAINDROP_SPEED
        
            
if __name__ == '__main__':
    # Instantiate the game and run it
    rocket_game = MainGame()
    rocket_game.run_game()