#import modules
import pygame as pg
from pygame.locals import *
from colour_palette import *


# draw shapes
def lindraw(screen, colour, x_pos_1, y_pos_1, x_pos_2, y_pos_2, width=1):
    """ draws line to screen """
    start_pos = (x_pos_1, y_pos_1)
    end_pos = (x_pos_2, y_pos_2)
    pg.draw.line(screen, colour, start_pos, end_pos, width)

def drawrec(screen, colour, x_pos, y_pos, width, height, n=0):
    """ draws rectangle (filled) to screen """
    rect = Rect(x_pos, y_pos, width, height)
    pg.draw.rect(screen, colour, rect, n)

def drawrecs(screen, colour, x_pos, y_pos, width, height, n):
    """ draws rectangle (outlined) to screen """
    rect = Rect(x_pos, y_pos, width, height)
    pg.draw.rect(screen, colour, rect, n)

def polydraw(screen, colour, x_pos_1, y_pos_1, x_pos_2, y_pos_2):
    """ draws polygon (filled) to screen """
    place = (x_pos_1, y_pos_1, x_pos_2, y_pos_2)
    pg.draw.polygon(screen, colour, place)

def polydraws(screen, colour, x_pos_1, y_pos_1, x_pos_2, y_pos_2, n):
    """ draws polygon (outlined) to screen """
    place = (x_pos_1, y_pos_1, x_pos_2, y_pos_2)
    pg.draw.polygon(screen, colour, place, n)
    
def elidraw(screen, colour, x_1, y_1, x_2, y_2):
    """ draws ellipse (filled) to screen """
    place = (x_1, y_1, x_2, y_2)
    pg.draw.ellipse(screen, colour, place)

def elidraws(screen, colour, x_1, y_1, x_2, y_2, n):
    """ draws ellipse (outlined) to screen """
    place = (x_1, y_1, x_2, y_2)
    pg.draw.ellipse(screen, colour, place, n)

if __name__ == '__main__':
    main()
