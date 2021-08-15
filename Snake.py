import pygame as pg
import random as rd
from pygame.locals import *
from pygame.time import Clock

def on_grid_random():
    x = rd.randint(0,590)
    y = rd.randint(0,590)
    return(x //10 *10, y//10 *10) 
    ## divisao inteira ##
def clollision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


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
apple_pos = on_grid_random()
apple = pg.Surface((10,10))
apple.fill((255,50,50))

Clock = pg.time.Clock()

while True:
    Clock.tick(20)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        if event.type ==KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT   

    if clollision(snake[0], apple_pos):
       apple_pos = on_grid_random()  
       snake.append((0,0)) 

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])            

    if my_direction == UP:
        snake[0] = (snake[0][0],snake[0][1]-10) ## (x , y)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1]+10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0]+10,snake[0][1])  
    if my_direction == LEFT:
        snake[0] = (snake[0][0]-10,snake[0][1])      

    screen.fill((0,0,0))
    screen.blit(apple ,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pg.display.update()
