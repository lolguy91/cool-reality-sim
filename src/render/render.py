import pygame
import system.preset

def RenderCircle(x,y,color,radius,surface):
    pygame.draw.circle(surface, color, (x,y), radius)
def RenderPreset(preset):
    x,y = (0,0)
    
    for part in preset.particles:
        x2,y2 = part.coords
        if x < x2:
            x = x2 + 30
        if y < y2:
            y = y2 + 30
        if x2 < 0 and abs(x2) > (x / 2):
            x = (abs(x2)* 2) + 30
        if y2 < 0 and abs(y2) > (y / 2):
            y = (abs(y2)* 2) + 30
            
    if x == 0:
        x = 40
    
    if y == 0:
        y = 40
        
    
    surface = pygame.Surface((x,y))
    print(x,y)
    defscl = x
    if y < x:
        defscl = y
    
    surface.fill((100,100,100))#clear the screen
    
    for part in preset.particles:
        if part.charge == 0:
            RenderCircle((x/2) + part.coords[0],(y/2) + part.coords[1],(128,128,128),defscl / 5,surface)
        elif part.charge > 0:
            RenderCircle((x/2) + part.coords[0],(y/2) + part.coords[1],(255,255,0),defscl / 5,surface)
        else:
            RenderCircle((x/2) + part.coords[0],(y/2) + part.coords[1],(0,0,255),defscl / 5,surface)
    
    return surface
def blit(src,dest,x,y,w,h):
    prect = pygame.Rect(x,y,w,h)                                                                        #position
    srect = pygame.Rect(0,0,x + w,y + h)                                                                    #size
    dest.blit(src,prect,srect)#draw the display to the screen
