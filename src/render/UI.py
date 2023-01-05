import pygame
import system.preset as preset
import render.render as render
import phisycs.particle as part
import phisycs.phisycs as phisycs

Ui = pygame.image.load('res/UI.png')


def init():
    pass

def update(surface,dt):
    #draw the background
    render.blit(Ui,surface,0,0,800,600)
    
    #Display the preset text
    font = pygame.font.Font('res/font.ttf', 23)
    text = font.render("presets:",True,(0,0,0),None)
    render.blit(text,surface,700,15,100,100)
    
    #Display the paused text if paused
    if phisycs.paused:
        font = pygame.font.Font('res/font.ttf', 100)
        text = font.render("PAUSED",True,(255,0,0),None)
        render.blit(text,surface,200,200,600,100)
        
    #draw the preset tray
    lol = render.RenderPreset(preset.Preset([part.mkelectron(0,0),part.mkproton(10,10)],"ass"))
    
    i = 0
    while(i < (2* 6)):
        x = 705 + ((i % 2)* 40) + ((i % 2)* 5)
        y = 55 + ((i / 2)* 40) + ((i / 2)* 5)
        render.blit(lol,surface,x,y,40,40)
        i+=1
     