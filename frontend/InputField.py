from utils import *
import frontend.debug as debug

class InputField:
    
    def __init__(self, x, y, width, height, name = "", color = (255,255,255)):

        



        self.x = x + 25
        self.y = y

        self.width = width - 25
        self.height = height

        self.radius = self.height / 2

        self.color = color

        self.name = name

        self.value = ""

        self.display_surface = pygame.display.get_surface()
        
        self.field = pygame.Rect((self.x,self.y),
                                (self.width,self.height))

        

        self.selected = False


    def CheckSelected(self):

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        if self.field.collidepoint(x,y):
            if self.selected:
                self.selected = False

            else:
                self.selected = True
        
        else:
            self.selected = False

        if(self.selected):
            self.color = (220,220,220)
        else:
            self.color = (200,200,200)
            

    def AddValue(self, val):
        self.value += val

    def RemoveLast(self):
        
        newValue = ""

        for n in range (len(self.value)-1):
            newValue += self.value[n]

        self.value = newValue


    def draw(self):

        pygame.draw.circle(self.display_surface,
                        self.color,
                        (self.x, self.y + self.height/2),
                        self.radius
                        )

        pygame.draw.rect(self.display_surface,
                        self.color,
                        self.field)

        pygame.draw.circle(self.display_surface,
                        self.color,
                        (self.x + self.width, self.y + self.height/2),
                        self.radius
                        )

        debug.debug(self.name, self.y + (self.height / 2 - 15),self.x - 125, (50,50,50))
        debug.debug(self.value, self.y + (self.height / 2 - 15), self.x, self.color)
