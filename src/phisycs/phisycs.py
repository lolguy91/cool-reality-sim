import phisycs.particle as particle
import math 

particles = []
def Coulomb(dist,c1,c2):
    return 8.98755e11 * ( c1*c2 ) / dist ** 2# !! it returns its result in Newtons
def N2MpS(F,M,dt):
    return (F/M)*dt
def dist2mag(dist,p1,p2,dt):
    distconv = dist / 2.25432e-13
    value = N2MpS(Coulomb(distconv,p1.charge,p2.charge),p1.mass,dt)# its in meters per second
    
    return (value * 2.25432e-13) / dt# our scale
#                   ^space scale   ^time scale
# Iok
#https://lolguy91-fantastic-eureka-gwgvpj4r654hw79r-6080.preview.app.github.dev/
#this is the intresting part, its the math, I asked ChatGPT for the formulas and values

def normalize(v):
       return (v[0] / math.sqrt(abs(v[0]**2 + v[0]**2)),v[1] / math.sqrt(abs(v[1]**2 + v[1]**2)))
    
#electromagnetism    
def applyEM(x,x2,y,y2, p1,p2,dt):

    xdiff = x2 - x
    ydiff = y2 - y
    
    if xdiff == 0 or ydiff == 0 : return (0,0)
    
    dist = math.dist([x,y], [x2,y2])
    
    dirx,diry = normalize((xdiff,ydiff))
    
    mag = dist2mag(dist,p1,p2,dt)
    
    return (dirx * mag,diry * mag)

def mkelectron(x,y):
    particles.append(particle.Particle((x,y),10,-1,9.10938e-31))

def mkproton(x,y):
    particles.append(particle.Particle((x,y),20,1,1.67262e-27))
    
def init():
    mkproton(0,0)
    
def update(dt):
    for particle in particles:
        if(particle.velocity != (0,0)):
            particle.velocity = normalize(particle.velocity)
        x,y = particle.coords
        
        for particle2 in particles:
            if particle2 == particle: continue
            
            x2,y2 = particle2.coords
            particle.velocity = (particle.velocity[0] - applyEM(x,x2,y,y2,particle,particle2,dt)[0],particle.velocity[1] - applyEM(x,x2,y,y2,particle,particle2,dt)[1])
    
    #it adds to the list if I use += like why? 
    particle.coords = ((particle.coords[0] + (particle.velocity[0] * dt)),(particle.coords[1] + (particle.velocity[1] *dt)))# python fucking sucks Im gonna get more ppl to work on this (on discord)
        
        