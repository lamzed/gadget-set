import pygame

pygame.init()
window = pygame.display.set_mode((960, 540))
bg = pygame.image.load("./images/bg.png")
window.blit(bg, (0, 0))  # 坐标点为左上角
kun = pygame.image.load("./images/kun.png")
window.blit(kun, (15, 250))
pygame.display.update()  # 注意此处是pygame，而不是window
clock = pygame.time.Clock()
# i=0
while True:
    clock.tick(60)
    # print(i)
    # i+=1
    pass
pygame.quit()
