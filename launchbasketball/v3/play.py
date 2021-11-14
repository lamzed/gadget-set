"""
    def kaishi(self):
        self.__cover()
        self.__loading()
        self.realkaishi = Timer(3,self.start)
        self.realkaishi.start() #不知为何，到了这步，虽然可以成功运行起来程序，但到进入下一步即start时，过几秒，程序就会卡死
"""
# import time
from basketball import *

pygame.init()
pygame.mixer.init()


class LaunchBasketball(object):

    def __init__(self):

        pygame.display.set_caption("BASKETBALL Launcher")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load("../sounds/cover.mp3")
        self.__create()
        # TODO pygame支持的bg最好ogg，音效即sound是wav
        # cover = pygame.mixer.Sound("../sounds/cover.mp3")
        # load = pygame.mixer.Sound("../sounds/jntm.mav")

    def start(self):

        # self.realkaishi.cancel()

        # print("test")
        self.__cover()
        self.__loading()
        pygame.time.delay(3000)
        pygame.time.set_timer(CHICKEN_EVENT, 1000)
        pygame.time.set_timer(KUN_FIRE_EVENT, 500)
        # ld = Timer(3.0,self.__loading())
        # ld.start()
        # self.__loading()

        while True:

            self.clock.tick(FRAME_PER_SEC)
            self.__handler()

            pygame.sprite.groupcollide(self.kun.basketball, self.chicken_group, True, True)
            bang = pygame.sprite.spritecollide(self.kun, self.chicken_group, True)
            if len(bang) > 0:
                # print(bang)
                # self.kun.kill()
                # LaunchBasketball.__game_over()
                # self.__overpg()
                break

            # self.__bang()
            self.__update()
            pygame.display.update()

        self.__overpg()

    def __cover(self):

        pygame.mixer.music.play()
        # cover.play()

        # i=1 封面循环
        while True:

            self.screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for kaishi in pygame.event.get():
                if kaishi.type == pygame.QUIT:
                    LaunchBasketball.__game_over()

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
        loadbg = pygame.mixer.Sound("../sounds/jntm.wav")
        loadbg.play()
        load = pygame.image.load("../images/load.png")
        self.screen.blit(load, (0, 0))
        pygame.display.update()
        # time.sleep(3)

    def __overpg(self):

        # print("loadpage")
        over = pygame.image.load("../images/over.png")
        self.screen.blit(over, (0, 0))
        pygame.display.update()

        while True:
            # print("2bcontinue")
            for jieshu in pygame.event.get():
                if jieshu.type == pygame.QUIT:
                    LaunchBasketball.__game_over()

            over_key = pygame.key.get_pressed()

            if over_key[pygame.K_SPACE]:
                # print("real over")
                LaunchBasketball.__game_over()

    def __create(self):

        cover = Cover()
        # TODO 游戏结束画面添加
        self.jiemian_group = pygame.sprite.Group(cover)

        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.kun = Kun()
        self.kun_group = pygame.sprite.Group(self.kun)

        self.chicken_group = pygame.sprite.Group()

    # def __bang(self):

    def __update(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        # self.kun.shanshuo.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.kun_group.update()
        self.kun_group.draw(self.screen)

        self.kun.basketball.update()
        self.kun.basketball.draw(self.screen)

        self.chicken_group.update()
        self.chicken_group.draw(self.screen)

        # self.jiemian_group.update()
        # self.jiemian_group.draw(self.screen)

    def __handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LaunchBasketball.__game_over()
            elif event.type == CHICKEN_EVENT:
                chickenz = Chicken()  # 初号鸡登场
                self.chicken_group.add(chickenz)
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
    def __game_over():
        print("GAMEOVER")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = LaunchBasketball()
    # print(dir(game))
    game.start()
