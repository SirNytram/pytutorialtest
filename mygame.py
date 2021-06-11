from pygameapp import *

class MyGame(GameApp):
    def __init__(self):
        super().__init__() 
        self.width = 1000
        self.myimage = None
        self.myFont = None
        self.myFontImage = None
        self.myText = None


    def on_start(self):
        self.myimage = GameImage('bluecar.png', (10,10))
        self.myFont = GameFont('Verdana',50)
        self.myText = GameText(self.myFont, 'mart is great', (125, 300), (255, 255, 125))
        # self.myFont = pygame.font.SysFont('Courier New', 25)
        # self.myFontImage = self.myFont.render('mytext', False, (255,255,125))
        
        
        #  pygame.image.load('bluecar.png')

    def on_loop(self):
        pass

    def on_render(self):
        self.myimage.render((100,100))
        self.myText.render()

        # self.surface.blit(self.myimage, (10,10))
        # self.surface.blit(self.myFontImage, (200,200))

    def on_event(self, eventId):
        pass

    def on_key(self, isDown, key, mod):
        if isDown == True and key == K_q:
            self.isRunning = False


if __name__ == "__main__" :
    MyGame().start()