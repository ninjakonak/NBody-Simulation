from utils import *
from BallProperties import BallProperties
import frontend.SideMenu as SideMenu
import frontend.debug as debug
from Simulator import Simulator

class Screen:

    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.surface=pygame.Surface(self.screen.get_size())
        self.surface=self.surface.convert()
        self.display_surface = pygame.display.get_surface()
    
        self.modes = ["add","select"]

        self.modeIndex = 0

        self.particles = []

        self.sideMenu = SideMenu.SideMenu()

        self.simulationRunning = False


    def CreateScreen(self):

        


        while True:

            self.Update()
            self.Render()

            


    def ScreenEventHandler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pos()[0] < self.sideMenu.x:

                    if self.modes[self.modeIndex] == "add":

                        if pygame.mouse.get_pressed()[0]:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            if(self.isDeployable(x,y)):
                                self.particles.append(BallProperties(x,y))

                    if self.modes[self.modeIndex] == "select":
                        self.ChangeSelectedParticle()

                        if self.SelectedParticleExists():
                            self.ChangeSideMenuProperties()

                        else:
                            self.sideMenu.ClearProperties()

                if pygame.mouse.get_pos()[0] > self.sideMenu.x:
                    self.sideMenu.SelectInputFields()
                    

            if event.type == pygame.KEYDOWN:
                self.checkKeyEvents(event.key)
                


    def checkKeyEvents(self, key):

        if key == pygame.K_w:
            self.modeIndex+=1

            if self.modeIndex >= len(self.modes):
                self.modeIndex = 0

        if key == pygame.K_f:
            for particle in self.particles:
                if particle.selected:
                    particle = self.sideMenu.GetNewParticle()

        if key == pygame.K_e:
            self.Simulator = Simulator(self.particles)
            self.simulationRunning = True

        field = self.sideMenu.GetSelectedInputField()
        if field != None:

            if key >= 48 and key <= 57 or chr(key) == '-':
                        
                field.AddValue(chr(key))
                    
            if key == 8:
                        
                field.RemoveLast()


    def drawObjects(self):
        if self.simulationRunning == False:
            for particle in self.particles:
                particle.draw()
        
    def SelectedParticleExists(self):
        for particle in self.particles:
            if particle.selected:
                return True

        return False

    def isDeployable(self,x,y):
        for particle in self.particles:
            if(x + RADIUS > particle.x - RADIUS and x - RADIUS < particle.x + RADIUS and y + RADIUS > particle.y - RADIUS and y - RADIUS < particle.y + RADIUS):
                return False
        return True

    def ChangeSelectedParticle(self):
        for particle in self.particles:
            particle.ChangeSelected()

        

    def findSelectedParticle(self):

        for particle in self.particles:
            if particle.IsSelected():
                return particle

        return None

    def ChangeSideMenuProperties(self):

        

        self.sideMenu.SetProperties(self.findSelectedParticle())

    def Update(self):
        self.ScreenEventHandler()

        if self.simulationRunning:
            self.Simulator.UpdateParticles()

    def Render(self):
        ClearScreen(self.display_surface)
        debug.debug("mode:"+self.modes[self.modeIndex],10,10,(128,128,128))
        self.drawObjects()
        if self.simulationRunning:
            self.Simulator.RenderParticles()
        self.sideMenu.draw()
        pygame.display.update()