import random

import pygame

SCREEN_RECT = pygame.Rect(0, 0, 960, 540)
FRAME_PER_SEC = 60
CHICKEN_EVENT = pygame.USEREVENT
KUN_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("E:/repositories/toolkit/src/main/resources/scripts/launchbasketball/images/bg.png", 1)
        # super().__init__("../images/bg.png", 1)
        if is_alt:
            # TODO 再次调用super方法，载入另一个背景
            self.rect.x = self.rect.width

    def update(self):
        super().update()
        if self.rect.x <= -SCREEN_RECT.width:
            self.rect.x = self.rect.width


class Cover(GameSprite):

    def __init__(self):
        super().__init__("E:/repositories/toolkit/src/main/resources/scripts/launchbasketball/images/cv.png", 0)
        # super().__init__("../images/cv.png", 0)

    def update(self):
        # print("update...")
        pass


class Kun(GameSprite):

    def __init__(self):
        super().__init__("E:/repositories/toolkit/src/main/resources/scripts/launchbasketball/images/kun.png", 0)
        # super().__init__("../images/kun.png", 0)
        # self.shanshuo = pygame.display.get_surface()
        self.rect.centery = SCREEN_RECT.centery
        self.rect.x = 52
        self.basketball = pygame.sprite.Group()

    def fire(self):
        for i in (0, 1, 2):
            bskb = Basketball()
            bskb.rect.left = self.rect.right + i * 33
            bskb.rect.centery = self.rect.centery - 11
            self.basketball.add(bskb)

    def update(self):

        self.rect.x += self.speed

        if self.rect.left < SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.top < SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top
        if self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom


class Basketball(GameSprite):

    def __init__(self):
        super().__init__("E:/repositories/toolkit/src/main/resources/scripts/launchbasketball/images/bskb.png", 4)
        # super().__init__("../images/bskb.png", 4)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= SCREEN_RECT.width:
            self.kill()


class Chicken(GameSprite):

    def __init__(self):
        super().__init__("E:/repositories/toolkit/src/main/resources/scripts/launchbasketball/images/chicken.png")
        # super().__init__("../images/chicken.png")
        self.speed = random.randint(2, 5)
        self.rect.x = SCREEN_RECT.width
        max_y = SCREEN_RECT.height - self.rect.height
        self.rect.y = random.randint(0, max_y)

    def update(self):
        super().update()
        if self.rect.x < - SCREEN_RECT.width:
            self.kill()

    def __del__(self):
        pass
