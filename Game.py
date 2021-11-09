# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:15:59 2021

@author: hugo_
"""

import pygame, copy, math, random

#Inicializacion de pygame
pygame.init()

#Tamaño del pixel
PIXEL_SIZE = 3
WIN_WIDTH = 640
WIN_HEIGHT = 480

#tiempo de las celulas
REFRESH = 20


TARGET_FPS = 60

#Grid de la pantalla
class Grid():
    def __init__(self):
        self.grid = [[False for i in range(int(WIN_HEIGHT / PIXEL_SIZE))] for i in range(int(WIN_WIDTH / PIXEL_SIZE))]

    def setCell(self, x, y, stat):
        self.grid[x][y] = stat
        
    def getCell(self, x, y):
        return self.grid[x][y]
     
    def countNeighbours(self, x, y):
        try:
            count = 0
            if self.getCell(x-1,y-1): count += 1
            if self.getCell(x,y-1): count += 1
            if self.getCell(x+1,y-1): count += 1
            if self.getCell(x-1,y): count += 1
            if self.getCell(x+1,y): count += 1
            if self.getCell(x-1,y+1): count += 1
            if self.getCell(x,y+1): count += 1
            if self.getCell(x+1,y+1): count += 1
            
        except:
            return 0

        return count


class debugText():
    def __init__(self, screen, clock, active_cells = 0, *args, **kwargs):
        self.screen = screen
        self.clock = clock
        self.active = active_cells
        self.font = pygame.font.SysFont("Monospaced", 20)
    
   
    def update(self, *args, **kwargs):
        self.screen = kwargs.get("screen",self.screen)
        self.clock = kwargs.get("clock",self.clock)
        self.active = kwargs.get("active",self.active)
 
 
def drawSquare(background, x, y):
    #Color de las celulas
    colour = (255), (255), (255)
    pygame.draw.rect(background, colour, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))       
