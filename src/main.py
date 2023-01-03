import pygame
import render.render as render
import render.particlerenderer as pr
import phisycs.phisycs as phisycs
import os

YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
phisycs.init()
def debug(dt):
    i = 0
    os.system("clear")
    print("==============Stats================")
    print("DeltaTime=",dt)
    print("============Particles==============")
    for particle in phisycs.particles:
        i+=1
        print("Particle #",i,":X=", int(particle.coords[0]),", Y=", int(particle.coords[1]),",Xvel=",particle.velocity[0],",Yvel=",particle.velocity[1])

def loop(dt):
    debug(dt)
    phisycs.update(dt)
    screen.fill((16,16,16))
    pr.renderParticles(screen)
    pygame.display.update()

lasttime = 0
running = True
while running:
    t = pygame.time.get_ticks()
    dt = (t - lasttime) / 1000.0
    lasttime = t
    if dt == 0:
        dt = 1
    loop(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            phisycs.mkelectron((event.pos[0]* pr.scale)- 400,(event.pos[1] * pr.scale) - 300)
pygame.quit()# https://lolguy91-fantastic-eureka-gwgvpj4r654hw79r-6080.preview.app.github.dev/
