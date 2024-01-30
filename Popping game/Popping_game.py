'''
Pygame for popping balloons
'''
__author__ = 'Soren Hecimovich'
__version__ = '01.23.2024'

import time

import pygame
import sys
import random

#object variables and gobles
done = False
points = 0
GREEN = (0, 255, 0)
balloons = []


#starts window stuff
pygame.init()
font = pygame.font.Font('hussar-font/HussarBoldCondensed-mmrV.otf', 40)
clock = pygame.time.Clock()
size = (700, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Popping Balloons')

#establishing images
sharp_image = pygame.image.load('img/scalpel.png').convert_alpha()
sharp = sharp_image.get_rect()
sharp.x = size[0]/2 - sharp.width/2
sharp.y = size[1]-80

blueballoon_image = pygame.image.load('img/blue balloon.png').convert_alpha()
blueballoon = blueballoon_image.get_rect()
blueballoon.x = random.randint(50, size[0]-120)
blueballoon.y = -10
bluegravity = random.randint(1,3)
#balloons.append(blueballoon)

pinkballoon_image = pygame.image.load('img/pink balloon.png').convert_alpha()
pinkballoon = pinkballoon_image.get_rect()
pinkballoon.x = random.randint(50, size[0]-120)
pinkballoon.y = -20
pinkgravity = random.randint(1,3)
#balloons.append(pinkballoon)

starballoon_image = pygame.image.load('img/star balloon.png').convert_alpha()
starballoon = starballoon_image.get_rect()
starballoon.x = random.randint(50, size[0]-120)
starballoon.y = -40
stargravity = random.randint(2,5)
#balloons.append(starballoon)

def message(msg, gameover):
    text = font.render(msg, True, GREEN)
    if not gameover:
        text_rect = text.get_rect(center=(size[0]-40, 30))
        screen.blit(text, text_rect)
    else:
        text_rect = text.get_rect(center=(size[0] // 2, size[1] // 2))
        screen.blit(text, text_rect)


#listnum = random.randint(0,2)
#balloon = balloons[listnum]
def makeballoon():
    listnum = random.randint(0, 2)
    balloon = balloons[listnum]
    randnum = random.randint(15, 675)
    screen.blit(balloon,(randnum, 0))
    balloonfloat = True
    while balloonfloat == True:
        balloon.x = randnum
        balloon.y = 0 + 1
        #pygame.display.update()
        balloonfloat = True
        if balloon.colliderect(sharp):
            balloonfloat = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sharp.left > 0:
        sharp.x -= 2
    if keys[pygame.K_RIGHT] and sharp.right < screen.get_width():
        sharp.x += 2
    screen.fill((0, 0, 0))
    blueballoon.y += bluegravity
    pinkballoon.y += pinkgravity
    starballoon.y += stargravity
    screen.blit(sharp_image, (sharp.x, sharp.y))
    screen.blit(blueballoon_image, (blueballoon.x, blueballoon.y))
    screen.blit(pinkballoon_image, (pinkballoon.x, pinkballoon.y))
    screen.blit(starballoon_image, (starballoon.x, starballoon.y))
    #BLUE BALLOON STUFF
    if blueballoon.colliderect(sharp):
        points = points + 1
        blueballoon.y = -100
        blueballoon.x = random.randint(50, size[0] - 120)
        bluegravity = random.randint(1,3)
    if pinkballoon.colliderect(sharp):
        points = points + 1
        pinkballoon.y = -100
        pinkballoon.x = random.randint(50, size[0] - 120)
        pinkgravity = random.randint(1,3)
    if starballoon.colliderect(sharp):
        points = points + 5
        stargravity = random.randint(3,6)
        starballoon.y = - 600
        starballoon.x = random.randint(50, size[0] - 120)
    if blueballoon.top > screen.get_height():
        print('Points:', points)
        done = True
    if pinkballoon.top > screen.get_height():
        print('Points:', points)
        done = True
    if starballoon.top > screen.get_height():
        starballoon.y = -1000
        stargravity = random.randint(1,2)

    message(str(points), done)
    pygame.display.flip()
    clock.tick(120)

screen.fill((0, 0, 0))
message(('Final score: '+str(points)), done)
pygame.display.flip()
time.sleep(2)
pygame.quit()
sys.exit()