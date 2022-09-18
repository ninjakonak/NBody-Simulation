from utils import *
import frontend.debug
import frontend.InputField as iField



class SideMenu:

    def __init__(self):
        self.x = 1000
        self.y = 0

        self.width = 500
        self.height = 750
        
        self.surface = pygame.display.get_surface()

        self.backgroundColor = (50,50,50)

        self.background = pygame.Rect((self.x,self.y),(self.width,self.height))

        self.inputColor = (200,200,200)

        self.InputFields = []

        self.InitInputFields()

        self.particle = None

        


    def InitInputFields(self):
        
        self.massInput = iField.InputField(self.x + 150, self.y + 100, 300, 50, "mass", self.inputColor)
        self.InputFields.append(self.massInput)

        self.vectorXInput = iField.InputField(self.x + 150, self.massInput.y+100, 300, 50, "vectorX", self.inputColor)
        self.InputFields.append(self.vectorXInput)
        
        self.vectorYInput = iField.InputField(self.x + 150, self.vectorXInput.y+100, 300, 50, "vectorY", self.inputColor)
        self.InputFields.append(self.vectorYInput)

        self.xInput = iField.InputField(self.x + 150, self.vectorYInput.y+100, 300, 50, "x position", self.inputColor)
        self.InputFields.append(self.xInput)

        self.yInput = iField.InputField(self.x + 150, self.xInput.y+100, 300, 50, "y position", self.inputColor)
        self.InputFields.append(self.yInput)
        
        
        
    def SetProperties(self, particle):
        self.particle = particle
        self.massInput.value = str(particle.mass)
        self.vectorXInput.value = str(particle.vectorX)
        self.vectorYInput.value = str(particle.vectorY)
        self.xInput.value = str(particle.x)
        self.yInput.value = str(particle.y)

    def ClearProperties(self):
        self.massInput.value = ""
        self.vectorXInput.value = ""
        self.vectorYInput.value = ""
        self.xInput.value = ""
        self.yInput.value = ""
        self.particle = None

    def GetNewParticle(self):
        self.particle.mass = int(self.massInput.value)
        self.particle.vectorX = int(self.vectorXInput.value)
        self.particle.vectorY = int(self.vectorYInput.value)
        self.particle.x = int(self.xInput.value)
        self.particle.y = int(self.yInput.value)

        return self.particle
   
    def SelectInputFields(self):

        for field in self.InputFields:
            field.CheckSelected()

    def GetSelectedInputField(self):

        for field in self.InputFields:
            if field.selected:
                return field

        return None
    

    def draw(self):
        pygame.draw.rect(self.surface,self.backgroundColor,self.background)
        
        self.massInput.draw()
        self.vectorXInput.draw()
        self.vectorYInput.draw()
        self.xInput.draw()
        self.yInput.draw()
        

