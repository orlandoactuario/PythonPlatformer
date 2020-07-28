import pygame as pg
from settings_salto import Settings
vec = pg.math.Vector2


# noinspection PyArgumentList
class Character(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        # Game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        # Image
        self.image_r = pg.image.load('Imagenes/Transparent/char.png')
        self.image_left = pg.image.load('Imagenes/Transparent/charizq.png')
        # self.image_jump = pg.image.load('Imagenes/Transparent/jump.png')
        self.image = self.image_r
        self.rect = self.image.get_rect()

        'Initialize position'
        self.rect.midbottom = self.screen_rect.midbottom
        self.pos = vec(self.settings.screen_width/2, self.settings.screen_height/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        'Flags'
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_count = -10

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.acc = vec(0, 0)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.acc.x = self.settings.char_accel

            # self.rect.x += self.settings.char_speed*min(self.acc, self.settings.char_topspeed)

        if self.moving_left and self.rect.left > 0:
            self.acc.x = -self.settings.char_accel

            # self.rect.x -= self.settings.char_speed*min(self.acc, self.settings.char_topspeed)

        if self.jumping:
            if self.jump_count == -10:  # This means we´re starting the jump
                self.currenty = self.rect.centery
                # self.image = self.image_jump
                self.pos.y = self.currenty + (self.jump_count ** 2 - 100)*2
                self.jump_count += .1
            elif -10 < self.jump_count < 10:
                # self.image = self.image_jump
                self.pos.y = self.currenty + (self.jump_count ** 2 - 100)*2
                self.jump_count += .1
            else:
                self.pos.y = self.currenty
                self.jumping = False
                self.jump_count = -10

        self.acc += self.vel * self.settings.char_friction
        self.vel += self.acc
        self.pos += self.vel + .5 * self.acc
        self.rect.center = self.pos


        # print(f'{self.acc} {self.vel} {self.pos} ')
        # self.rect.bottom = self.y


class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill((120, 50, 40))
        self.rect = self.image.get_rect()
        self.rect = x, y


