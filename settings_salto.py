class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 200, 230)

        # SALTO
        self.jump_frame = 20

        # Movement settings
        self.ship_limit = 3
        self.char_speed = 1
        self.char_accel = .2
        self.char_topspeed = 3
        self.char_friction = -.02




