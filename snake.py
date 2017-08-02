import turtle
from time import sleep
from random import randrange
from msvcrt import getch, kbhit

class Snake(turtle.Turtle):
    """My Snake turtle"""
    pos = [0, 0]
    count = 0
    total = 0
    pastpos = []
    pastkey = 72
    wn = turtle.Screen()

    def __init__(self,*args,**kwargs):
        super(Snake,self).__init__(*args,**kwargs)
        print("Time for my turtle snake!")
        self.up()
        self.speed(0)
        self.shape('circle')

    def gameover(self):
        self.pos[0] = 0
        self.pos[1] = 0
        self.count = 1
        self.total = 0
        cs = 1
        if (len(self.pastpos)) > 39:
            cs = 2
        for i in range(len(self.pastpos)// cs):
            del self.pastpos[0]
            self.wn.bgcolor('red')
            sleep(0.03)
            self.clearstamps(cs)
            self.wn.bgcolor('white')
            sleep(0.03)
        self.pastpos = []
        self.setposition(self.pos[0], self.pos[1])
        

    def changepos(self, dirc, neg):
        if dirc == 'X':
            if neg == '-':
                self.pos[0] += -10
            else:
                self.pos[0] += 10

        if dirc == 'Y':
            if neg == '-':
                self.pos[1] += -10
            else:
                self.pos[1] += 10
    def begin(self):
        print("to start game press any key")
        key = ord(getch())
        print("START")

    def pause(self):
        print("paused")
        print('to exit press esc')
        print("to resume press any key")
        key = ord(getch())
        if key == 27:
            print("EXITED")
            return 27
        print("resumed")
        

    def getkey(self):
        if kbhit() == 0:
            key = self.pastkey
            sleep(0.01)
        else:
            key = ord(getch())
        if key == 27: #ESC
            key = self.pause()
            if key == 27:
                return 27
        if key == 80: #Down arrow
            self.changepos('Y', '-')
        elif key == 72: #Up arrow
            self.changepos('Y', '+')
        elif key == 75: #Left arrow
            self.changepos('X', '-')
        elif key == 77: #Right arrow
            self.changepos('X', '+')
        else:
            self.getkey()
        if key == 80 or key == 72 or key == 75 or key == 77:
            self.pastkey = key

class Food(turtle.Turtle):
    """Snakes Food"""
    def __init__(self,*args,**kwargs):
        super(Food,self).__init__(*args,**kwargs)
        print("Time for FOOD!")
        self.up()
        self.speed(0)
        self.shape('circle')
        self.turtlesize(0.7, 0.7)
        self.color('red')
        self.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)

    def setpos(self):
        self.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)
