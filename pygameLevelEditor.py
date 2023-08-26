import pygame as pg

pg.init()

#Game Window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LOWER_MARGIN = 100
SIDE_MARGIN = 300

run = True

screen = pg.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN , SCREEN_HEIGHT + LOWER_MARGIN))

pg.display.set_caption('Level Editor')

#Background images scrolling
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,0,0)

#Images
# bg1 = pg.image.load('Images/bg1.png').convert_alpha()
# bg2 = pg.image.load('Images/bg2.png').convert_alpha()
bg_sky = pg.image.load('Images/sky.png').convert_alpha()
bg_mountain = pg.image.load('Images/mountain.png').convert_alpha()


def draw_Background():
    screen.fill(GREEN)
    width = bg_sky.get_width()
    for x in range(4):
        screen.blit(bg_sky,((width*x)-scroll,0))
        screen.blit(bg_mountain,((width*x)-scroll,SCREEN_HEIGHT - bg_mountain.get_height()))

while run:

    draw_Background()

    if scroll_left == True:
        scroll -= 5
    if scroll_right == True:
        scroll += 5

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                scroll_left = True
            if event.key == pg.K_RIGHT:
                scroll_right = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    scroll_left = False
                if event.key == pg.K_RIGHT:
                    scroll_right = False 
 
    pg.display.update()

pg.quit()

