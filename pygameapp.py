import pygame, pygame.display, pygame.surface
from pygame.locals import *



class GameImage():
    def __init__(self, fileName = None, position = (0,0)):
        self.image = None
        self.fileName = fileName
        self.position =  position

    def load(self):
        if self.fileName:
            self.image = pygame.image.load(self.fileName).convert()

    def blit(self, positionparm = None):
        if positionparm != None:
            self.position = positionparm

        pygame.display.get_surface().blit(self.image, self.position)



    def rotate(self, angle, centerOfRotation=None):
        if centerOfRotation == None:
            self.image = pygame.transform.rotate(self.image, angle)
        else:
            pass






class GameFont():
    def __init__(self, name, size):
        self.font = None
        self.name = name
        self.size = size

    def load(self):
        self.font = pygame.font.SysFont(self.name, self.size)

class GameText(GameImage):
    def __init__(self, font, text = '', position = (0,0), color = (0,0,0)):
        super().__init__(None, position)
        self.font = font
        self.text = text
        self.color = color

    def blitText(self, text, position = None):
        self.text = text
        self.blit(position)

    def blit(self, position = None):
        if self.text != '':
            self.image = self.font.font.render(self.text, True, self.color)
        super().blit(position)

class GameApp:
    def __init__(self):
        self.running = True
        self.surface = None
        self.width = 640
        self.height = 480
        self.fps = 10
        # self.objlist = []
        self.keysPressed = None
        self.curUserEvent = USEREVENT 
        self.clock = None

 


    def on_start(self):
        pass
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_event(self, eventType):
        pass


    def cleanup(self):
        pygame.quit()
 
    def addTimer(self, mili, once = False):
        self.curUserEvent += 1
        pygame.time.set_timer(self.curUserEvent, mili, once)
        return self.curUserEvent
    
    def start(self):
        pygame.init()

        self.surface = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
 
        self.on_start()
        while( self.running ):
            self.keysPressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.on_event(event.type)


            self.on_loop()

            self.on_render()
            pygame.display.update()
            self.clock.tick(self.fps)
 
if __name__ == "__main__" :
    theApp = PyGameApp()
    theApp.start()
