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

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
 
pg.quit()

