import pygame
import random
pygame.init()
win = pygame.display.set_mode((550, 550))
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)
pygame.display.set_caption('XO')
run  = True
x = 1
while x < 100:
    color = [random.randrange(1, 255),random.randrange(1, 255),random.randrange(1, 255)]
    position = [random.randrange(50, 100), random.randrange(110, 500)]
    pygame.draw.circle(win,color,position, 10)
    x+=1
    
color = [random.randrange(1, 255),random.randrange(1, 255),random.randrange(1, 255)]
position = [(400,300),(200,500),(2,5), (100,500)]
eliprect = pygame.Rect(100,200, 300, 100)
pygame.draw.ellipse(win,color,eliprect,0)
pygame.draw.polygon(win,color,position, 10)
        
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # win.fill([0,123,19])
            print(event.pos)
            
        if event.type == pygame.KEYDOWN:
            print(event.unicode)    
            if event.unicode == 'x':
                print("print osods ")
            
    pygame.display.update()
pygame.quit()   
