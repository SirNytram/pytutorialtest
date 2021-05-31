import pygame, pygame.display, pygame.surface
from pygame.locals import *

     
class PyGameApp:
    def __init__(self):
        self.running = True
        self.surface = None
        self.width = 640
        self.height = 480
        self.fps = 60
        # self.objlist = []
 
 
    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False


    def on_loop(self):
        pass
    def on_render(self):
        pass

    def on_start(self):
        pass


    def cleanup(self):
        pygame.quit()
 
    
    def start(self):

        pygame.init()
        self.surface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
 
        self.on_start()
        while( self.running ):
            for event in pygame.event.get():
                self.process_event(event)
            self.on_loop()
            # for obj in self.objlist:
            #     obj.render()
            self.on_render()
            pygame.display.update()
            pygame.time.Clock().tick(self.fps)
 
if __name__ == "__main__" :
    # theApp = PyGameApp()
    PyGameApp().start()
    # theApp.on_execute()
