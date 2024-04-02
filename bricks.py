import pygame


class bricks():
    def __init__(self,i):
        self.img = pygame.image.load("./image/brick.png")
        self.position = [self.img.get_size()[0] * i,305]
        self.show = True
        
    def run(self,speed):
        self.position[0] -= speed 
        
    def drop(self,chara):
        if self.ischaradrop(chara):
            chara.life = False
            
    def ischaradrop(self,chara):
        if not self.show:
            if chara.position[1] >= 210:
                    if abs(chara.position[0] + chara.img[0].get_size()[0] - self.position[0] - self.img.get_size()[0]) < 5:
                        return True
        return False
        
    