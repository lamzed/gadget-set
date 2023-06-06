import random
import pygame
#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,960,540)
#刷新的频率
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄发射子弹事件
KUN_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):
        #调用父类的初始化方法
        super().__init__()
        #定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #在屏幕的垂直方向上移动
        self.rect.x -= self.speed

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #1. 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("../images/chicken.png")
        #2. 指定敌机的初始随机速度
        self.speed = random.randint(2,5)
        #3. 指定敌机的初始随机位置
        self.rect.x = SCREEN_RECT.width
        #TODO 使得飞机出场时位于屏幕中间，两条蓝色遮幅中间
        max_y = SCREEN_RECT.height - self.rect.height
        #max_y = self.rect.y
        self.rect.y = random.randint(0,max_y)

    def update(self):
        #1. 调用父类方法，保持水平方向的飞行
        super().update()
        #self.rect.x += self.speed

        #2. 判断是否飞出屏幕，t若是，需要从精灵组删除敌机
        if self.rect.x <= -SCREEN_RECT.width:
            #print("敌机飞出屏幕...")
            #kill方法可以将精灵从所有精灵组中移除，精灵就会被自动销毁
            self.kill()

    def __del__(self):
        #print("敌机挂了... %s" % self.rect)
        pass

class Kun(GameSprite):
    """琨"""
    def __init__(self):
        #1. 调用父类方法，设置image&speed
        super().__init__("../images/kun.png",0)
        #2. 设置英雄的初始位置
        self.rect.centery = SCREEN_RECT.centery
        self.rect.x = 52
        #3. 创建子弹精灵组
        self.basketball = pygame.sprite.Group()

    def launch(self):
        #print("jjjjj")
        for i in (0,1,2):
            #1. 创建子弹精灵
            bskb = Basketball()
            #2. 设置精灵的位置
            bskb.rect.left = self.rect.right + i * 33
            bskb.rect.centery = self.rect.centery - 11
            #3. 将精灵添加到精灵组
            self.basketball.add(bskb)

    def update(self):
        #英雄在水平方向移动
        self.rect.x += self.speed
        #控制英雄不能离开屏幕
        #if self.rect.x < 0:
            #self.rect.x = 0
        if self.rect.left < SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.top < SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

class Basketball(GameSprite):

    def __init__(self):
        """子弹精灵"""
        #调用父类方法，设置子弹图片，设置初始速度
        super().__init__("../images/bskb.png",4)

    def update(self):
        #（教学中。。调用父类方法），让子弹沿水平方向飞行
        self.rect.x += self.speed
        if self.rect.x > SCREEN_RECT.width:
            self.kill()

    def __del__(self):
        print("子弹销毁...")

class Background(GameSprite):

    def __init__(self,is_alt=False):
        #1. 调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__("../images/bg.png",1)
        #2. 判断是否是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.x = self.rect.width

    def update(self):
        #1. 调用父类的方法实现
        super().update()
        #2. 判断是否移除屏幕，若移除屏幕，将图像设置到屏幕的上方
        if self.rect.x <= -SCREEN_RECT.width:
            self.rect.x = self.rect.width
