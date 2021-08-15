import pygame as pg
import random as rd
import json

from pygame.locals import *
from pygame.time import Clock

def on_grid_random():
    x = rd.randint(0,590)
    y = rd.randint(0,590)
    return(x //10 *10, y//10 *10) 
    ## divisao inteira ##

def collision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

### feito o sistema de pontos ###
def Ponts(ponts,c1,c2):
    if  collision(c1,c2) == True:
        return (ponts +1)
    else :
        return (ponts +0)    

def function_wall():
    for i in range(0,600,10):
        screen.blit(wall,(0,i))
        screen.blit(wall,(590,i))
        screen.blit(wall,(i,0))
        screen.blit(wall,(i,590))
    #g.fill(255,10,10)

#font = pg.Font.SysFont('Arial', 20)
#ponts_text = font.render('Score: ', False, (200,200,190))   

#def print_score():
 #   ponts_value = font.render(str(ponts), False, (255,255,255))
  #  screen.blit(ponts_text,(20,550))
   # screen.blit(ponts_value,(100,550))

   

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pg.init()
screen = pg.display.set_mode((600,600))
pg.display.set_caption('Snake')

wall = pg.Surface((10,10))
wall.fill((200,200,200))
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
ponts = int(0)

game_over = False

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

    if collision(snake[0], apple_pos):
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
    
    for i in snake[1:]:
        if collision(snake[0],i):
            game_over = True;
            break

    if (snake[0][0] <= 0 or snake[0][0] >= 590 or snake[0][1] <= 0 or snake[0][1] >= 590):
        game_over = True

    function_wall()
    #print_score()
    ponts = Ponts(ponts,snake[0],apple_pos)
    
    if game_over:
        break
    
    #print(ponts)
    pg.display.update()
    

