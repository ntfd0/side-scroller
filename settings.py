class Settings:
    def __init__(self):
        """Settings constants"""
        self.GAME_TITLE = 'Fanteria'
        self.GAME_BACKGROUND_COLOR = (255, 255, 255)
        self.CHAR_SPEED = 2.5
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.BULLET_SPEED = 10
        self.BULLET_COLOR = (75, 0, 130)
        self.BULLET_WIDTH = 15
        self.BULLET_HEIGHT = 3
        self.MAX_BULLETS = 10

        self.TEXT_COLOR = (255, 255, 255)
        self.BACKGROUND_COLOR = (0, 0, 255)

        self.COUNTER_FONT_SIZE = 55

        self.RAINDROP_SPEED = 1
        # Leave 1/3 of the screen as buffer space
        self.RAINDROP_START_X = int(self.SCREEN_WIDTH / 1.1)
        self.RAINDROP_END_X = self.SCREEN_WIDTH
        self.RAINDROP_START_Y = 0 + self.BULLET_HEIGHT * 2
        self.RAINDROP_END_Y = self.SCREEN_HEIGHT - self.BULLET_HEIGHT * 2

        self.MAX_RAINDROPS = 10