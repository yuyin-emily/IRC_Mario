import pygame
import datetime

pygame.init()
pygame.display.set_caption("Mario")
screen = pygame.display.set_mode((640,360))
clock = pygame.time.Clock()
clock.tick(55)
background = pygame.image.load("background.png")

running = True

while running:
    time = datetime.datetime.now().second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    print(time)
    
    for i in range(5):
        screen.blit(background,[i * 160,0])

    pygame.display.update()

