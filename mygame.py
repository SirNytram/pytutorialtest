
from gameapp import *

class MyRedCar(GameImage):
    def __init__(self):
        super().__init__("images\\redcar.png", (200, 300))
        self.bRightSide = True

    def move(self):
        if self.bRightSide:
            super().move(1, 0);
        else:
            super().move(-1, 0)

class MyGame(GameApp):
    def __init__(self):
        super().__init__() 
        self.width = 1000
        self.myimage = None
        self.myFont = None
        self.myFontImage = None
        self.myText = None
        self.redcar = MyRedCar()
        self.fps = 50


    def on_start(self):
        self.imgCar = GameImage('images\\bluecar.png', (10,500))
        # self.redcar = 
        self.myFont = GameFont('Verdana',50)
        self.myText = GameText(self.myFont, 'mart is great', (125, 300), (255, 255, 125))
        
        
        #  pygame.image.load('bluecar.png')

    def on_loop(self):
        self.imgCar.move(y=-5)
        if self.imgCar.position[1] < 5:
            self.imgCar.position = (10,500)

        self.redcar.move()

    def on_render(self):
        self.surface.fill((100 ,100,255))
        self.imgCar.render()
        self.myText.text = str(self.clock.get_time())
        self.myText.render()
        self.redcar.render()


    def on_event(self, eventId):
        pass

    def on_key(self, isDown, key, mod):
        if isDown == True and key == K_q:
            self.isRunning = False

        if isDown == True and key == K_t:
            self.redcar.bRightSide = not self.redcar.bRightSide


if __name__ == "__main__" :
    MyGame().start()