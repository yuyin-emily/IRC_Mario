import pygame

class bricks():
    def __init__(self,i):
        self.img = pygame.image.load("./image/brick.png")
        self.position = [self.img.get_size()[0] * i,305]
        
    def run(self,speed):
        self.position[0] -= speed 
        