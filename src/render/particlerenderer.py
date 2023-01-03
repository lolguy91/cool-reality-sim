import render.render as render
import phisycs.phisycs as phisycs

scale = 1
    
def renderParticles(surface):
    for part in phisycs.particles:
        if part.charge == 0:
            render.RenderCircle(400 + (part.coords[0] / scale),300 + (part.coords[1] / scale),(128,128,128),20 /scale,surface)
        elif part.charge > 0:
            render.RenderCircle(400 + (part.coords[0] / scale),300 + (part.coords[1] / scale),(255,255,0),20 /scale,surface)
        else:
            render.RenderCircle(400 + (part.coords[0] / scale),300 + (part.coords[1] / scale),(0,0,255),10 / scale,surface)
