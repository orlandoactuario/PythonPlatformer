import time
import pygame as pg
import sys
from settings_salto import Settings
from character import Character
from character import Platform


class Game:

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.char = Character(self)
        self.plat = pg.sprite.Group()
        p1 = Platform(0, self.settings.screen_height - 100, self.settings.screen_width, self.settings.screen_height - 100)
        self.plat.add(p1)

    def run_game(self):
        while True:
            self.check_events()
            self.char.update()
            self._update_screen()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pg.K_ESCAPE:
            sys.exit()
        if not self.char.jumping:
            if event.key == pg.K_SPACE:
                self.char.jumping = True
                self.char.jump_count = -10
            if event.key == pg.K_RIGHT:
                self.char.moving_right = True
                self.char.image = self.char.image_r
            if event.key == pg.K_LEFT:
                self.char.moving_left = True
                self.char.image = self.char.image_left

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.char.moving_right = False
        elif event.key == pg.K_LEFT:
            self.char.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.plat.draw(self.screen)
        self.char.blitme()
        pg.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = Game()
    ai.run_game()
