import pygame, pygame.display, pygame.surface
from pygame.locals import *



class GameImage():
    def __init__(self, fileName = None, position = (0,0)):
        self.image = None
        self.fileName = fileName
        self.position =  position
        if self.fileName:
            self.image = pygame.image.load(self.fileName).convert()

    def render(self, position = None):
        if position != None:
            self.position = position

        pygame.display.get_surface().blit(self.image, self.position)



    def rotate(self, angle, centerOfRotation=None):
        if centerOfRotation == None:
            self.image = pygame.transform.rotate(self.image, angle)
        else:
            pass


class GameFont():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.font = pygame.font.SysFont(self.name, self.size)

class GameText():
    def __init__(self, font, text = '', position = (0,0), col = (0,0,0)):
        self.image = None
        self.position =  position

        self.font = font
        self.text = text
        self.color = col

    def renderText(self, text, position = None):
        self.text = text
        self.render(position)

    def render(self, position = None):
        if position != None:
            self.position = position

        if self.text != '':
            self.image = self.font.font.render(self.text, True, self.color)
            pygame.display.get_surface().blit(self.image, self.position)

class GameApp:
    def __init__(self):
        self.isRunning = True
        self.surface = None
        self.width = 640
        self.height = 480
        self.isFullScreen = False
        self.fps = 100
        self.keysPressed = []
        self.curUserEventId = USEREVENT 
        self.clock = None
 


    def on_start(self):
        pass
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_event(self, eventId):
        pass
    def on_key(self, isDown, key, mod):
        pass


    def cleanup(self):
        pygame.quit()
 
    def addTimer(self, mili, runOnce = False):
        self.curUserEventId += 1
        pygame.time.set_timer(self.curUserEventId, mili, runOnce)
        return self.curUserEventId
    
    def start(self):
        pygame.init()





        self.surface = pygame.display.set_mode((self.width, self.height))
        if self.isFullScreen == True:
            pygame.display.toggle_fullscreen()

        self.clock = pygame.time.Clock()
 
        self.on_start()
        while( self.isRunning ):
            self.keysPressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

                self.on_event(event.type)

                if event.type == KEYDOWN:
                    self.on_key(True, event.key, event.mod)
                if event.type == KEYUP:
                    self.on_key(False, event.key, event.mod)
                


            self.on_loop()
            self.on_render()

            pygame.display.update()
            self.clock.tick(self.fps)
 

if __name__ == "__main__" :
    
    GameApp().start()
