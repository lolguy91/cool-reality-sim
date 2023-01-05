import phisycs.phisycs as phisycs
class Preset:
    name = ""
    particles = []
    def __init__(self,_particles,_name):
        self.particles = _particles
        self.name = _name
 
def PlacePreset(preset,ox,oy):
    for part in preset.particles:
        partcpy = part
        partcpy.coords = (ox + part.coords[0],oy  + part.coords[1])
        phisycs.particles.append(partcpy)