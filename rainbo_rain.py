#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.



#import modules
import sys
from random import randint, gauss, choice
import pygame as pg
from colour_palette import *
from utils import *


#initalise
pg.init()


def main():
    
    #variables
    width = 1920
    height = 1080

    screen = pg.display.set_mode((width, height), FULLSCREEN)
    pg.mouse.set_visible(False)

    heightmod_a = 0
    heightmod_b = 20
    heightmod_c = 40
    heightmod_d = 60
    height_a = randint(heightmod_a, heightmod_b)
    height_b = randint(heightmod_c, heightmod_d)
    height_delim = height
    bg_a = 0
    bg_b = 0
    bg_c = 0
    bg_col = (bg_a, bg_b, bg_c)
    fill_palette = 0

    amb_snd = pg.mixer.Sound("rain.wav")
    amb_snd.play()

    col_lis = []
    def addlis(col):
        for x in col[::-1]:
            col_lis.append(x)
        for x in col:
            col_lis.append(x)

    col_li = [
            red_palette, orange_palette, 
            yellow_palette, green_palette, 
            blue_palette, violet_palette,
            cyan_palette, colour_list,
            ]

    for x in col_li:
        addlis(x)

    sel_col_lis = col_lis
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_j:
                    sel_col_lis = green_palette

        screen.fill(bg_col)
        
        
        col_lis = []
        def addlis(col):
            for x in col[::-1]:
                col_lis.append(x)
            for x in col:
                col_lis.append(x)
        
        col_li = [
                red_palette, orange_palette, 
                yellow_palette, green_palette, 
                blue_palette, violet_palette,
                cyan_palette, colour_list,
                ]
        
        for x in col_li:
            addlis(x)
         
        lin_width = 1
        switch = 90
        gauss_a = 20
        gauss_b = 1340
        randheight_a = randint(0, 660)
        set_tilt = 20
        
        set_lin_width_up = False
        set_lin_width_down = False
        set_switch_up = False
        set_switch_down = False
        set_tilt_amount_left = False
        set_tilt_amount_right = False


        while True:
            for y in range(1, 4):
                colour = choice(col_lis[::-1])
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            pg.quit()
                            sys.exit()
                        elif event.key == pg.K_SPACE:
                            screen.fill(BLACK)
                            pg.display.update()
                        elif event.key == pg.K_DOWN:
                            set_switch_down = True
                        elif event.key == pg.K_UP:
                            set_switch_up = True
                        elif event.key == pg.K_w:
                            fill_palette = 1
                        elif event.key == pg.K_s:
                            fill_palette = 0
                        elif event.key == pg.K_a:
                            set_lin_width_down = True
                        elif event.key == pg.K_d:
                            set_lin_width_up = True
                        elif event.key == pg.K_LEFT:
                            set_tilt_amount_left = True
                        elif event.key == pg.K_RIGHT:
                            set_tilt_amount_right = True

                    if event.type == pg.KEYUP:
                        set_lin_width_up = False
                        set_lin_width_down = False
                        set_switch_up = False
                        set_switch_down = False
                        set_tilt_amount_left = False
                        set_tilt_amount_right = False

                if set_lin_width_up:
                    lin_width += 1
                    if lin_width >= 10:
                        lin_width = 10
                if set_lin_width_down:
                    lin_width -= 1
                    if lin_width <= 1:
                        lin_width = 1
                if set_switch_up:
                    switch += 2
                    if switch >= 90:
                        switch = 90
                if set_switch_down:
                    switch -= 2
                    if switch <= 0:
                        switch = 0
                if set_tilt_amount_left:
                    set_tilt -= 7
                if set_tilt_amount_right:
                    set_tilt += 7

                randheight_a =  randint(0, 660)
                randsq = randint(20, 1300)
                randsqu = randint(25, 100)
                for x in range(randint(200, 720)):
                    w_a = gauss(gauss_a, gauss_b)
                    lindraw(screen, colour, w_a - set_tilt, height_a, w_a + set_tilt, height_b, lin_width)
                    lindir = 'down'
                    if lindir == 'down':
                        height_a += randheight_a
                        height_b += randheight_a
                        if height_b >= height_delim:
                            height_a = randint(heightmod_a, heightmod_b)
                            height_b = randint(heightmod_c, heightmod_d)

                pg.time.wait(switch)
                pg.display.update()
                if fill_palette == 1:
                    pass
                elif fill_palette == 0:
                    screen.fill(bg_col)

        pg.display.update()

if __name__ == '__main__':
    main()
