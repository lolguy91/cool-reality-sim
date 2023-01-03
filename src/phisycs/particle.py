

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
        
        