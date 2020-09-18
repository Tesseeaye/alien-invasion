class Settings:
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.fullscreen = False
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 5

        # Ship settings
        self.ship_speed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet directiom of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Sound settings
        self.sound_effects = 0.25