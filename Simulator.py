from Grav import Particle
import pygame


class Simulator:
    

    def __init__(self, particles: list):

        self.particles = []

        self.surface = pygame.display.get_surface()
        
        for particle in particles:
            self.particles.append(Particle(particle.x, 
                                           particle.y, 
                                           particle.mass*10**13, 
                                           particle.vectorX*10**13, 
                                           particle.vectorY*10**13))

    
    #particles.append(Ball((screen_width/2),(screen_height/2),10**25,0,0))
    #particles.append(Ball(screen_width/8,(screen_height/2),10**14,0,7*10**19))


    def UpdateParticles(self):
        for i in self.particles:

            for j in self.particles:
                
                if not j==i:
                    x=float(j.x)
                    y=float(j.y)
                    m=float(j.m)
                    i.move(x,y,m)
                    if i.collided:
                        if i in self.particles:
                            self.particles.remove(i)
                        self.particles.remove(j)

    def RenderParticles(self):

        for particle in self.particles:
            pygame.draw.circle(self.surface,
                               particle.color,
                               (particle.x,particle.y),
                               particle.radius)