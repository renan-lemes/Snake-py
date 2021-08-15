import pygame as pg
import random as rd
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pg.init()
screen = pg.display.set_mode((600,600))
pg.display.set_caption('Snake')

## a snake vai ser uma lista de seguimentos e uma dupla ##
snake = [(200,200), (210,200),(220,200)]
snake_skin = pg.Surface((10,10))
snake_skin.fill((0,255,80))
my_direction = LEFT
##  desenho da maça   ##
apple_pos = (rd.randint(0,590),rd.randint(0,590))
apple = pg.Surface((10,10))
apple.fill((255,50,50))

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
    screen.fill((0,0,0))
    screen.blit(apple ,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pg.display.update()
