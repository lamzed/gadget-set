import pygame
import sys
import traceback

pygame.init()
pygame.mixer.init()

bg_size = width, height = 960,540
screen = pygame.display.set_mode(bg_size)

pygame.display.set_caption("测试是否是标题")

background = pygame.image.load("../images/bg,png")

pygame.mixer.music.load("")

