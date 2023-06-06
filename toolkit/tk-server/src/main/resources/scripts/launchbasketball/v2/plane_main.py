import pygame
from plane_sprite import *
#from . import plane_sprite

class PlaneGame(object):
    """plane game"""
    
    def __init__(self):
        print("initializing...")
        #1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2. 创建游戏时钟
        self.clock = pygame.time.Clock()
        #3. 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        #4. 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(KUN_FIRE_EVENT,500)
    
    def start_game(self):
        print("starting...")
        while True:
            #1.设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()
    
    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #print("乌鸦坐飞机")
                #创建敌机精灵
                enemy1 = Enemy()
                #将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy1)
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                #print("right")
            elif event.type == KUN_FIRE_EVENT:
                self.kun.launch()

        #使用键盘提供的方法获取键盘按键 - 键盘元组
        keys_pressed = pygame.key.get_pressed()
        #判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            #print("right...")
            self.kun.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.kun.speed = -2
        #elif keys_pressed[pygame.K_RIGHT,pygame.K_LEFT]:
            #self.kun.speed = 0
        elif keys_pressed[pygame.K_UP]:
            self.kun.rect.y -= 2
        elif keys_pressed[pygame.K_DOWN]:
            self.kun.rect.y += 2
        else:
            self.kun.speed = 0

    def __check_collide(self):
        
        #1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.kun.basketball,self.enemy_group,True,True)
        #2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.kun,self.enemy_group,True)
        if len(enemies) > 0:
            self.kun.kill()
            PlaneGame.__game_over()
    
    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.kun_group.update()
        self.kun_group.draw(self.screen)

        self.kun.basketball.update()
        self.kun.basketball.draw(self.screen)
    
    @staticmethod
    def __game_over():
        print("-"*24)
        print("GAMEOVER")
        pygame.quit()
        exit()
    
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        #bg2.rect.x = bg2.rect.width
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        #创建英雄的精灵和精灵组
        self.kun = Kun()
        self.kun_group = pygame.sprite.Group(self.kun)

if __name__ == "__main__":
    #创建游戏对象
    game = PlaneGame()
    #启动游戏
    game.start_game()
