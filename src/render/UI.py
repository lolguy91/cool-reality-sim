import pygame
Ui = pygame.image.load('res/UI.png')

def init():
    pass

def update(surface,dt):
    prect = pygame.Rect(0,0,0,0)                                                                        #position
    srect = pygame.Rect(0,0,800,600)                                                                    #size
    surface.blit(Ui,prect,srect)