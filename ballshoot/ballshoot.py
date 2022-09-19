import configparser
import os
import random

import pygame

pygame.init()
pygame.mixer.init()

'''
'''
dirname = os.path.dirname(os.path.abspath(__file__))

ini = os.path.join(dirname, "ballshoot.ini")
cfg = configparser.RawConfigParser()
cfg.read(ini)

settings = "settings"
bg = cfg.get(settings, "bg")
debut_pic = cfg.get(settings, "debut_pic")
jntm = cfg.get(settings, "jntm")
debut_muz = cfg.get(settings, "debut_muz")

SCREEN_RECT = pygame.Rect(0, 0, 960, 540)
FRAME_PER_SEC = 60
CHICK_EVENT = pygame.USEREVENT
KUN_FIRE_EVENT = pygame.USEREVENT + 1


class BALLSHOOT(object):

    def __init__(self):
        pygame.display.set_caption("BALLSHOOT")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load(debut_muz)
        self.__create()
        # TODO pygame支持的bg最好ogg，音效即sound是wav

    def start(self):
        self.__cover()
        self.__loading()
        pygame.time.delay(3000)
        pygame.time.set_timer(CHICK_EVENT, 1000)
        pygame.time.set_timer(KUN_FIRE_EVENT, 500)
        # ld = Timer(3.0,self.__loading())
        # ld.start()
        # self.__loading()

        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__handler()
            pygame.sprite.groupcollide(self.kun.basketball, self.chick_group, True, True)
            bang = pygame.sprite.spritecollide(self.kun, self.chick_group, True)
            if len(bang) > 0:
                # print(bang)
                # self.kun.kill()
                # LaunchBasketball.__game_over()
                # self.__over()
                break

            # self.__bang()
            self.__update()
            pygame.display.update()

        self.__over()

    def __cover(self):
        pygame.mixer.music.play()
        # cover.play()

        # i=1 封面循环
        while True:
            self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for kaishi in pygame.event.get():
                if kaishi.type == pygame.QUIT:
                    BALLSHOOT.__gameover()

            start_key = pygame.key.get_pressed()

            if start_key[pygame.K_SPACE]:
                pygame.mixer.music.stop()
                break

            self.clock.tick(67)
            # TODO 载入画面
            self.jiemian_group.update()
            self.jiemian_group.draw(self.screen)
            # print("i")
            # i+=1
            # self.screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            pygame.display.update()

    def __loading(self):

        # TODO 替换鸡你太美音频。au打开wma格式再重新导出MP3格式，现有的MP3格式直接是修改wma后缀名所得

        # load.play()
        # timer = pygame.time.get_ticks()
        # print(timer)

        pygame.mixer.init()
        song = pygame.mixer.Sound(jntm)
        song.play()
        load = pygame.image.load(debut_pic)
        self.screen.blit(load, (0, 0))
        pygame.display.update()
        # time.sleep(3)

    def __over(self):
        over = pygame.image.load("images/over.png")
        self.screen.blit(over, (0, 0))
        pygame.display.update()

        while True:
            for over in pygame.event.get():
                if over.type == pygame.QUIT:
                    BALLSHOOT.__gameover()

            over_key = pygame.key.get_pressed()

            if over_key[pygame.K_SPACE]:
                # print("real over")
                BALLSHOOT.__gameover()

    def __create(self):
        cover = Cover()
        # TODO 游戏结束画面添加
        self.jiemian_group = pygame.sprite.Group(cover)

        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.kun = Kun()
        self.kun_group = pygame.sprite.Group(self.kun)

        self.chick_group = pygame.sprite.Group()

    # def __bang(self):

    def __update(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.kun_group.update()
        self.kun_group.draw(self.screen)

        self.kun.basketball.update()
        self.kun.basketball.draw(self.screen)

        self.chick_group.update()
        self.chick_group.draw(self.screen)

    def __handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                BALLSHOOT.__gameover()
            elif event.type == CHICK_EVENT:
                chick = Chick()
                self.chick_group.add(chick)
            elif event.type == KUN_FIRE_EVENT:
                self.kun.fire()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            # self.kun.speed = 2
            self.kun.rect.x += 4
        if keys_pressed[pygame.K_LEFT]:
            # self.kun.speed = -2
            self.kun.rect.x -= 4
        if keys_pressed[pygame.K_UP]:
            self.kun.rect.y -= 4
        if keys_pressed[pygame.K_DOWN]:
            self.kun.rect.y += 4

    @staticmethod
    def __gameover():
        print("GAMEOVER")
        pygame.quit()
        exit()


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
        super().__init__(bg, 1)
        if is_alt:
            # TODO 再次调用super方法，载入另一个背景
            self.rect.x = self.rect.width

    def update(self):
        super().update()
        if self.rect.x <= -SCREEN_RECT.width:
            self.rect.x = self.rect.width


class Cover(GameSprite):

    def __init__(self):
        super().__init__("images/cover.png", 0)

    def update(self):
        # print("update...")
        pass


class Kun(GameSprite):

    def __init__(self):
        super().__init__("images/kun.png", 0)
        # self.shanshuo = pygame.display.get_surface()
        self.rect.centery = SCREEN_RECT.centery
        self.rect.x = 52
        self.basketball = pygame.sprite.Group()

    def fire(self):
        for i in (0, 1, 2):
            ball = Ball()
            ball.rect.left = self.rect.right + i * 33
            ball.rect.centery = self.rect.centery - 11
            self.basketball.add(ball)

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


class Ball(GameSprite):

    def __init__(self):
        super().__init__("images/ball.png", 4)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= SCREEN_RECT.width:
            self.kill()


class Chick(GameSprite):

    def __init__(self):
        super().__init__("images/chick.png")
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


if __name__ == "__main__":
    game = BALLSHOOT()
    game.start()
