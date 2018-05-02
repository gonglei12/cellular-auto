# -*- coding: utf-8 -*-
import pygame
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('image\\ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (self.width-self.rect.width)//2, \
                                        (self.height-self.rect.height)//2
        
        self.speed_x, self.speed_y = 3., 4.
        self.speed = math.sqrt(self.speed_x**2+self.speed_y**2)
        self.mass = 10
        
        
    def move(self):
        #print('ta-da: %d, %d' % (self.speed_y, self.rect.top))
        if self.rect.top<0 or self.rect.bottom>self.height:
            self.speed_y = self.speed_y * (-1)
        if self.rect.left<0 or self.rect.right>self.width:
            self.speed_x *= -1
        self.rect.move_ip(self.speed_x, self.speed_y)

    def faster(self, ort, a=1):
        if ort == 'up':
            self.speed_y -= a
        elif ort == 'down':
            self.speed_y += a
        elif ort == 'left':
            self.speed_x -= a
        elif ort == 'right':
            self.speed_x += a
        else:
            pass
        

        

        
            