import pygame

class bricks():
    def __init__(self,i):
        self.img = pygame.image.load("./image/brick.png")
        self.position = [self.img.get_size()[0] * i,305]
        self.show = True
        
    def run(self,speed):
        self.position[0] -= speed 
        
    def drop(self,chara,chara_position):
        if not self.show and chara_position[1] >= 210 and chara_position[0] > self.position[0] and chara_position[0] < self.position[0] + self.img.get_size()[0] // 4: #條件1:blocks.show = True, 條件2:chara[y] >= 210, 條件3:chara[x]位於範圍內
            chara.life = False
        
    