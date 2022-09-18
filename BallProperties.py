from utils import *

class BallProperties:


    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.vectorX = 0
        self.vectorY = 0

        self.mass = 0

        self.surface = pygame.display.get_surface()
        self.selected = False
        self.radius = 5
        self.color = (255,255,255)


    def ChangeSelected(self):
        
        mouse_pos=pygame.mouse.get_pos()
        
        if mouse_pos[0]>=self.x-self.radius and mouse_pos[0] < self.x + self.radius and mouse_pos[1]>=self.y-self.radius and mouse_pos[1] < self.y + self.radius and mouse_pos[0]<1000:
            if not self.selected:
                self.selected = True
                self.color = (255,0,0)
                return True
            else:
                self.selected = False
                self.color = (255,255,255)
                return False
        else:
            self.selected = False
            self.color = (255,255,255)
            return False


    def IsSelected(self):
        return self.selected


    def draw(self):
        pygame.draw.circle(self.surface,
                           self.color,
                           (self.x,self.y),
                           self.radius)
