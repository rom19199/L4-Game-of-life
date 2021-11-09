# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:15:17 2021

@author: hugo_
"""
import pygame, copy, math, random

from Game import *

#Inicializacion de pygame
pygame.init()

#Tamaño del pixel
PIXEL_SIZE = 3
WIN_WIDTH = 640
WIN_HEIGHT = 480

#tiempo de las celulas
REFRESH = 20


TARGET_FPS = 60

def main():
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    clock = pygame.time.Clock()

    isActive = True
    actionDown = False
    
    final = pygame.time.get_ticks()
    grid = Grid()  
    debug = debugText(screen, clock)  

    for x in range(0, int(WIN_WIDTH / PIXEL_SIZE)):
        for y in range(0, int(WIN_HEIGHT / PIXEL_SIZE)):
            if random.randint(0, 10) == 1:
                grid.setCell(x, y, True)
                drawSquare(background, x, y)

    screen.blit(background, (0, 0)) 
    pygame.display.flip()

    while isActive:
        clock.tick(TARGET_FPS)
        newgrid = Grid()

        if pygame.time.get_ticks() - final > REFRESH:
            numActive = 0
            background.fill((0, 0, 0))

            for x in range(0, int(WIN_WIDTH / PIXEL_SIZE)):
                for y in range(0, int(WIN_HEIGHT / PIXEL_SIZE)):
                    if grid.getCell(x, y):
                        if grid.countNeighbours(x, y) < 2:
                            newgrid.setCell(x, y, False)

                        elif grid.countNeighbours(x, y) <= 3:
                            newgrid.setCell(x, y, True)
                            numActive += 1
                            drawSquare(background, x, y)

                        elif grid.countNeighbours(x, y) >= 4:
                            newgrid.setCell(x, y, False)

                    else:
                        if grid.countNeighbours(x, y) == 3:
                            newgrid.setCell(x, y, True)
                            numActive += 1
                            drawSquare(background, x, y)

            final = pygame.time.get_ticks() 

        else:
            newgrid = grid
            
        debug.update(active = numActive)

        actionDown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isActive = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                actionDown = True

                while actionDown:
                    newgrid.setCell(pygame.mouse.get_pos()[0] / PIXEL_SIZE, 
                    	pygame.mouse.get_pos()[1] / PIXEL_SIZE, True)
                    	
                    drawSquare(background, pygame.mouse.get_pos()[0] / PIXEL_SIZE, 
                    	pygame.mouse.get_pos()[1] / PIXEL_SIZE)
                    
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            actionDown = False
                    
                    screen.blit(background, (0, 0)) 
                    pygame.display.flip()

        grid = newgrid       

        screen.blit(background, (0, 0)) 
        debug.update(active = numActive)
        pygame.display.flip()
       
if __name__ == "__main__":
    main()