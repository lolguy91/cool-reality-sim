import pygame
import render.render as render
import render.UI as Ui
import render.particlerenderer as pr
import phisycs.phisycs as phisycs
import os

def left_click(x,y):
    phisycs.mkelectron((x* pr.scale)- 400,(y * pr.scale) - 300)
def middle_click(x,y):
    phisycs.mkneutron((x* pr.scale)- 400,(y * pr.scale) - 300)
def right_click(x,y):
    phisycs.mkproton((x* pr.scale)- 400,(y * pr.scale) - 300)

def debug(dt):
    i = 0
    os.system("clear")
    print("==============Stats================")
    print("DeltaTime=",dt)
    print("============Particles==============")
    for particle in phisycs.particles:
        i+=1
        print("Particle #",i,":X=", int(particle.coords[0]),", Y=", int(particle.coords[1]),",Xvel=",particle.velocity[0],",Yvel=",particle.velocity[1])
def Render():
    screen.fill((16,16,16))#clear the screen
    
    display.fill((16,16,16))#clear the display(where the particles are showing)
    
    pr.renderParticles(display)#render the stuff
    
    prect = pygame.Rect(0,0,0,0)                                                                        #position
    srect = pygame.Rect(0,0,690,481)                                                                    #size
    screen.blit(display,prect,srect)#draw the display to the screen
    
    Ui.update(screen,dt)#add the UI

def loop(dt):
    debug(dt)
    phisycs.update(dt)
    Render()
    pygame.display.update()

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
display = pygame.Surface((800,600))

phisycs.init()
Ui.init()


lasttime = 0
running = True
while running:
    t = clock.tick(24)
    dt = (t - lasttime) / 1000.0
    
    lasttime = t
    if dt == 0:
        dt = 1
    loop(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click(event.pos[0],event.pos[1])
            if event.button == 2:
                middle_click(event.pos[0],event.pos[1])
            if event.button == 3:
                right_click(event.pos[0],event.pos[1])
            
pygame.quit()# https://lolguy91-fantastic-eureka-gwgvpj4r654hw79r-6080.preview.app.github.dev/
