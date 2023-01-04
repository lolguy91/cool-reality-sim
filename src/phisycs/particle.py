

class Particle:
    coords = (0,0)
    velocity = (0,0)
    mass = 0
    radius = 0
    charge = 0
    def __init__(self,_coords,_radius,_charge,_mass,_startvel):
        self.coords = _coords
        self.radius = _radius
        self.charge = _charge
        self.mass = _mass
        self.velocity = _startvel
        
def mkelectron(x,y,_startvel = (0,0)):
    return Particle((x,y),10,-1,9.10938e-31,_startvel)
    
def mkproton(x,y,_startvel = (0,0)):
    return Particle((x,y),20,1,1.67262e-27,_startvel)

def mkneutron(x,y,_startvel = (0,0)):
    return Particle((x,y),20,0,1.67262e-27,_startvel)
        
        