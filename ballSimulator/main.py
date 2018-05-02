# -*- coding: utf-8 -*-

import pygame, sys, traceback, ball
from pygame.locals import *

pygame.init()
pygame.mixer.init()

bg_size = bg_width, bg_height = 600, 480
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('BallSimulator')

background = 255,255,255



def main():
    clock = pygame.time.Clock()
    #generate a ball
    ball1 = ball.Ball(bg_size)
    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            ball1.faster('up')
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            ball1.faster('left')
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            ball1.faster('down')
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            ball1.faster('right')
        
        ball1.move()
        screen.fill(background)
        screen.blit(ball1.image, ball1.rect)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        
        
if __name__=='__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
