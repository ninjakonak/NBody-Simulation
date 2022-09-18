from utils import *

class Particle:
    def __init__(self,x,y,m,vecx,vecy):
        self.x=x
        self.y=y
        self.m=m


        self.dt=0.001
        self.momentum=[vecx,vecy]
        print(self.momentum)
        self.g=6.67*10**-11

        self.color=(255,255,255)
        self.radius=RADIUS
        self.collided=False

    def calcdistx(self,x):
        return x-self.x

    def calcdisty(self,y):
        return y-self.y

    def calcdist(self,x,y):
        return math.sqrt((self.calcdistx(x))**2+(self.calcdisty(y))**2)

    def calcgravitationalpull(self,m,x,y):
        return (self.g*self.m*m)/self.calcdist(x,y)**2

    def calcangle(self,A,B,C):
        return acos((A * A + B * B - C * C)/(2.0 * A * B))

    def calcmomentum(self,x,y,m):
        theta=math.atan2(y-self.y,x-self.x)
        force=self.calcgravitationalpull(m,x,y)

        force_x=math.cos(theta)
        force_y=math.sin(theta)
        
        self.momentum[0]+=force_x*force
        self.momentum[1]+=force_y*force
        self.x+=self.momentum[0]/self.m*self.dt
        self.y+=self.momentum[1]/self.m*self.dt
    
    def move(self,x2,y2,m2):
        
        self.calcmomentum(x2,y2,m2)

        
        if self.calcdist(x2,y2)<=RADIUS:
            self.collided=True

    def draw(self,surface):
        coor=self.x,self.y
        pygame.draw.circle(surface,self.color,coor,self.radius)
