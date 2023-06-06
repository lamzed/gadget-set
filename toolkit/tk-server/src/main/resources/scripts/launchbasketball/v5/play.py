from basketball import *


class LaunchBasketball(object):

    def __init__(self):

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create()
        pygame.time.set_timer(CHICKEN_EVENT, 1000)
        pygame.time.set_timer(KUN_FIRE_EVENT, 500)

    def start(self):

        self.__cover()

        while True:
            self.clock.tick(FRAME_PER_SEC)
            # self.__cover()
            self.__handler()
            self.__bang()
            self.__update()
            pygame.display.update()

    def __cover(self):

        # i=1 封面循环
        while True:

            for kaishi in pygame.event.get():
                if kaishi.type == pygame.QUIT:
                    LaunchBasketball.__game_over()

            start_key = pygame.key.get_pressed()

            if start_key[pygame.K_SPACE]:
                break

            self.clock.tick(30)
            # TODO 载入画面
            self.jiemian_group.update()
            self.jiemian_group.draw(self.screen)
            # print("i")
            # i+=1
            pygame.display.update()

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

    def __bang(self):

        pygame.sprite.groupcollide(self.kun.basketball, self.chicken_group, True, True)

        bang = pygame.sprite.spritecollide(self.kun, self.chicken_group, True)
        if len(bang) > 0:
            # print(bang)
            self.kun.kill()
            LaunchBasketball.__game_over()

    def __update(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

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
            self.kun.rect.x += 2
        if keys_pressed[pygame.K_LEFT]:
            # self.kun.speed = -2
            self.kun.rect.x -= 2
        if keys_pressed[pygame.K_UP]:
            self.kun.rect.y -= 2
        if keys_pressed[pygame.K_DOWN]:
            self.kun.rect.y += 2

    @staticmethod
    def __game_over():
        print("GAMEOVER")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = LaunchBasketball()
    # print(dir(game))
    game.start()
