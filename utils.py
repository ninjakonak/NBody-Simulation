import pygame,math,time
import sys
from math import acos, degrees
import pygame


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750
RADIUS = 5

def ClearScreen(surface):
    pygame.draw.rect(surface,(128, 128, 128),pygame.Rect((0,0),(SCREEN_WIDTH,SCREEN_HEIGHT)))