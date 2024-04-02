import pygame

class golds():
    def __init__(self):
        self.position = [355,250]
        self.img = [pygame.image.load("./image/ggl.png"),
                  pygame.image.load("./image/ggr.png")
                  ]
        self.show = True
    
    def eat(self,chara_position):
        if abs(chara_position[0] - self.position[0]) < 20 and abs(chara_position[1] - self.position[1]) < 50: 
            self.show = False
            
    def run(self):
        self.position[0] -= 10
        
    def setPosition(self,i):
        self.show = True
        if i < 5:
            if i == 2:
               self.position = [200 + 50 * i, 160]
            else:
                self.position = [200 + 50 * i, 250]
        else:
            if i == 7:
                self.position = [500 + 50 * i, 160]
            else:
                self.position = [500 + 50 * i, 250]