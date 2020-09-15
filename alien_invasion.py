import sys

import pygame as py

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Main class that will initiate the game."""

    def __init__(self):
        """Start the game, and create the window."""
        py.init()
        self.settings = Settings()

        # uncomment if you want to run in windowed mode.
        # self.screen = py.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.screen = py.display.set_mode((0, 0), py.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        py.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = py.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_events()
        
    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in py.event.get():
            if event.type == py.QUIT:
                sys.exit()
            elif event.type == py.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == py.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == py.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == py.K_LEFT:
            self.ship.moving_left = True
        elif event.key == py.K_SPACE:
            self._fire_bullet()
        elif event.key == py.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == py.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == py.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

            # Laser sound effect by sharesynth from freesound.org
            laser_sound = py.mixer.Sound('sounds/laser.wav')
            laser_sound.set_volume(self.settings.sound_effects)
            laser_sound.play()

    def _update_bullets(self):
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_events(self):
        # Redraw the screen during each pass through of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        py.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()