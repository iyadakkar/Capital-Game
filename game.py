from typing import Any
from pygame import *
from random import randint

from pygame.sprite import *
mixer.init()
#create game window
window = display.set_mode((700,500))
#set scene background
display.set_caption('Ping Pong')
#creat 2 sprites and place them on the scene
background=transform.scale(image.load('white.jpg'),(700,500))
win_width=700
win_height=500
lost=0

class game_sprite (sprite.Sprite):
    def __init__(self, images,speed,rect_y,rect_x,sx,sy):
        super().__init__()
        self.image=transform.scale(image.load(images),(sx,sy))
        self.speed= speed
        self.rect=self.image.get_rect()
        self.rect.x= rect_x
        self.rect.y= rect_y
        
    def reset(self): 
        window.blit(self.image,(self.rect.x,self.rect.y)) 


class paddle(game_sprite):
    def update(self):
        
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_w] and self.rect. y >=10:
            self.rect.y-=self.speed
        if keys_pressed[K_s] and self.rect. y<=250:

            self.rect.y+=self.speed

class paddle1(game_sprite):
    def update(self):
        
        keys_pressed=key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect. y >=10:
            self.rect.y-=self.speed
        if keys_pressed[K_DOWN] and self.rect. y<=250:

            self.rect.y+=self.speed
     

 
paddle3 = paddle('paddle.png',17,200,10,50,250)
paddle2= paddle1('paddle.png',17,200,650,50,250)
        
 
game = True 
while game:
  
    for e in event.get():
        if e.type==QUIT:
            game=False
         

        
    window.blit(background,(0,0))
    

    paddle3.reset()
    paddle3.update()
    paddle2.reset()
    paddle2.update()


    time.delay(50)
    display.update()