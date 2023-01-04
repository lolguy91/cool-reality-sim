import phisycs.particle as particle
import math
import numpy as np



particles = []
def CoulombEM(dist,c1,c2):
    return (8.98755e11 * ( c1*c2 )) / (dist ** 2)# !! it returns its result in Newtons
def CoulombG(dist,m1,m2):
    return (6.674e-11 * m1*m2 ) / (dist ** 2)# !! it returns its result in Newtons
def N2MpS(F,M,dt):
    return (F/M)*dt
def dist2magEM(dist,p1,p2,dt):
    distconv = dist * 4435927463714.113
    value = N2MpS(CoulombEM(distconv,p1.charge,p2.charge),p1.mass,dt)# its in meters per second
    
    return (value / 4435927463714.113) / dt# our scale
#                   ^space scale   ^time scale
def dist2magG(dist,p1,p2,dt):
    distconv = dist * 4435927463714.113
    value = N2MpS(CoulombG(distconv,p1.mass,p2.mass),p1.mass,dt)# its in meters per second
    
    return (value / 4435927463714.113) / dt# our scale
#                   ^space scale   ^time scale

def normalize(v):
       return (v[0] / math.sqrt(abs(v[0]**2 + v[0]**2)),v[1] / math.sqrt(abs(v[1]**2 + v[1]**2)))
    
#electromagnetism    
def applyEM(x,x2,y,y2, p1,p2,dt):

    xdiff = x2 - x
    ydiff = y2 - y
    
    if xdiff == 0 or ydiff == 0 : return (0,0)
    
    dist = math.dist([x,y], [x2,y2])
    
    dirx,diry = normalize((xdiff,ydiff))
    
    mag = dist2magEM(dist,p1,p2,dt)
    
    return (dirx * mag,diry * mag)

def applyG(x,x2,y,y2, p1,p2,dt):

    xdiff = x2 - x
    ydiff = y2 - y
    
    if xdiff == 0 or ydiff == 0 : return (0,0)
    
    dist = math.dist([x,y], [x2,y2])
    
    dirx,diry = normalize((xdiff,ydiff))
    
    mag = dist2magG(dist,p1,p2,dt)
    
    return (dirx * mag,diry * mag)

def addelectron(x,y,_startvel = (0,0)):
    particles.append(particle.Particle((x,y),10,-1,9.10938e-31,_startvel))

def addproton(x,y,_startvel = (0,0)):
    particles.append(particle.Particle((x,y),20,1,1.67262e-27,_startvel))
    
def addneutron(x,y,_startvel = (0,0)):
    particles.append(particle.Particle((x,y),20,0,1.67262e-27,_startvel))
    
def init():
    add_hydrogen(0,0)
    

def add_hydrogen(ox,oy):
    addproton(ox,oy)
    addneutron(ox+10,oy+20)
    addelectron(ox+200,oy,   calculate_orbit_velocity(200,0))

def calculate_orbit_velocity(x,y):
    c = x + y * 1j
    a = np.abs(c)
    c /= a
    angle = np.log(c) / (2j * np.pi)
    vel = 10
    return (math.sin(angle) * vel,math.cos(angle) * vel)
    

def update(dt):
    for particle in particles:
        x,y = particle.coords
        
        for particle2 in particles:
            if particle2 == particle: continue
            
            x2,y2 = particle2.coords
            
            em = applyEM(x,x2,y,y2,particle,particle2,dt)
            g =  applyG(x,x2,y,y2,particle,particle2,dt)
            particle.velocity = (particle.velocity[0] - em[0] - g[0],particle.velocity[1] - em[1] - g[1])
    
        particle.coords = (particle.coords[0] + (particle.velocity[0] * dt),particle.coords[1] + (particle.velocity[1] *dt))# python fucking sucks
        
        