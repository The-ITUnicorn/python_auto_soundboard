import pygame
import os
import time
from PIL import Image

font_name = pygame.font.match_font('arial')
def text_objects(text, font, textColor):
    textSurface = font.render(text, True, textColor)
    return textSurface, textSurface.get_rect()

display_width = 800
display_height = 600


#############
##COLORS#####
#############
black = (0,0,0)
white = (255,255,255)
felt = (7,182,13)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
blue = (0,0,255)