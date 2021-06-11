# from typing import List
from pygameapp import GameApp, GameImage, GameFont, GameText
import pygame.key, pygame.surface, pygame.display, pygame.transform
#from pygame import key
from pygame.locals import *
import json


class TopArrow():
    def __init__(self, parent, direction, xposition, key):
        super().__init__() 
        self.parent = parent
        self.direction = direction  #'left', right, up, down
        # self.isPressed = False
        self.xposition = xposition
        self.defaultImage = GameImage(self.direction + "_default.png", (self.xposition, 10))
        self.pressedImage = GameImage(self.direction + "_pressed.png", (self.xposition, 10))
        self.key = key

    def load(self):
        self.defaultImage.load()
        self.pressedImage.load()


    def is_pressed(self):
        if self.parent.keysPressed[self.key]:
            return True
        else:
            return False

    def render(self):

        if self.is_pressed():
            self.pressedImage.blit()
        else:
            self.defaultImage.blit()
            

class Line():
    def __init__(self, parent):
        self.parent = parent
        self.yposition = 300
        self.arrow1image = GameImage("left_default.png")
        self.speed = 0.5

    def load(self):
        self.arrow1image.load()

    def render(self):
        self.arrow1image.blit((20, self.yposition))
        
    def move(self):
    
        self.yposition -= (self.speed * 1)

        if self.parent.keysPressed[K_UP]:
            self.arrow1image.rotate(180)


class FunkinApp(GameApp):
    # variable creation
    def __init__(self):
        super().__init__() 
        self.fps = 60
        self.toparrowList = []

        self.movingline = Line(self)

        self.width = 800
        self.height = 600
        self.testfont =  None
        self.myText = None
        self.tickText = None
        self.numSecsText = None
        self.msText = None
        self.numSecs = 0
        self.numSecsTimerId = None
        self.tick = 0
        self.ms = 0

    # game load
    def on_start(self):
        myArrow = TopArrow(self, 'left', 10, K_LEFT)
        self.toparrowList.append(myArrow)
        self.toparrowList.append(TopArrow(self, 'left', 100, K_RIGHT))

        self.testfont =  GameFont("Verdana", 20)
        self.myText = GameText(self.testfont)
        self.tickText = GameText(self.testfont)
        self.numSecsText = GameText(self.testfont)
        self.msText = GameText(self.testfont, '', (200,400) )


        f = open('tutorialfile.json') 
        songfile = json.load(f)
        print(songfile['song']['song'])
        for section in songfile['notes']:
            print(section['mustHitSection'])
            # print(section['mustHitSection'])
            for notes in section['sectionNotes']:
                print(notes)

        self.numSecsTimerId = self.addTimer(1000, True)
        self.testfont.load()

        for arrow in self.toparrowList:
            arrow.load()
        self.movingline.load()


    # game logic
    def on_loop(self):
        if self.keysPressed[K_ESCAPE]:
            self.running = False

        if self.keysPressed[K_r]:
            self.movingline.yposition = 300
            

        self.movingline.move()

        self.tick += 1

    # game display
    def on_render(self):
        #display background
        self.surface.fill((255, 255, 255))
        
        # display arrows
        for arrow in self.toparrowList:
            arrow.render()

        self.movingline.render()

        #diplay some text
        self.myText.text = 'fps:' + str(self.clock.get_fps())
        self.myText.blit((500,500))

        # self.numSecsText.text = str(self.numSecs)
        # self.numSecsText.blit((400,500))
        self.numSecsText.blitText(str(self.numSecs), (400,500))

        self.tickText.blitText('tick:' + str(self.tick), (200,450))
        self.ms += self.clock.get_time()
        self.msText.blitText('ms:' + str(self.ms))
        

    def on_event(self, eventid):
        if eventid == self.numSecsTimerId:
            self.numSecs += 1

            self.movingline.arrow1image.rotate(45)

if __name__ == "__main__" :

    # myapp = FunkinApp()
    # myapp.start()
    FunkinApp().start()
