import pygame

import bricks
import charas

def isbricksrun(brick,keys,chara_position):
    if brick.position[0] >= 640 - brick.img.get_size()[0]:
        if keys[pygame.K_RIGHT]:
            if chara_position > 500:
                return True
    return False

pygame.init()
pygame.display.set_caption("Mario")
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()

background = pygame.image.load("./image/background.png")

running = True
num=0

brick = []
for i in range(24): 
    brick.append(bricks.bricks(i))
chara = charas.charas() 

brick[5].show = False
brick[10].show = False
brick[15].show = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    num+=1
    keys = pygame.key.get_pressed()
    
    if isbricksrun(brick[23],keys,chara.position[0]):
        for i in range(24):
            brick[i].run(chara.speed)
    else:
        chara.run(keys)
        
    chara.jumping()
    
    for i in range(24):
        brick[i].drop(chara,chara.position)
        
    running=chara.down()
    
    for i in range(5):
        screen.blit(background,[i * 160,0])
        
    for i in range(24):
        if brick[i].show:
            screen.blit(brick[i].img,brick[i].position)

    if chara.dirX == "right":
        screen.blit(chara.img[(num % 80) // 40],chara.position)
    else:
        screen.blit(chara.img[(num % 80) // 40 + 2],chara.position) 
        
    clock.tick(55)
    pygame.display.update()