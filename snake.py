import turtle
from time import sleep
from random import randrange
from msvcrt import getch, kbhit

class Snake(turtle.Turtle):
    """My Snake turtle"""
    pos = [0, 0]
    count = 0
    total = 2
    pastpos = []
    pastkey = 72
    wn = turtle.Screen()

    def __init__(self, diff, *args,**kwargs):
        super(Snake,self).__init__(*args,**kwargs)
        print("Creating Snake... \n DONE")
        self.up()
        self.speed(0)
        self.shape('circle')
        self.diff = diff
        if self.diff == 4:
            self.total = 20
        self.settime()

    def reset(self):
        self.settime()
        self.pos = [0, 0]
        self.count = 0
        self.total = 2
        if self.diff == 4:
            self.total = 20
        self.pastpos = []
        self.setposition(self.pos[0], self.pos[1])

    def settime(self):
        if self.diff == 1:
            self.time = 0.04
        elif self.diff == 2:
            self.time = 0.01
        else:
            self.time = 0.000001

    def border(self):
        self.setpos(-250, -250)
        self.down()
        for i in range(4):
            self.forward(500)
            self.left(90)
        self.up()
        self.setpos(0, 0)

    def gameover(self):
        self.pos[0] = 0
        self.pos[1] = 0
        self.count = 0
        if self.diff == 4:
            self.total = 20
        self.total = 2
        cs = 1
        if (len(self.pastpos)) > 39:
            cs = 2
        if (len(self.pastpos)) > 100:
            cs = 5
        for i in range(len(self.pastpos)// cs):
            del self.pastpos[0]
            self.wn.bgcolor('red')
            sleep(self.time)
            self.clearstamps(cs)
            self.wn.bgcolor('white')
            sleep(self.time)
        self.clearstamps()
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
        
    def getkey(self):
        sleep(self.time)
        if kbhit() == 0:
            key = self.pastkey
        else:
            key = ord(getch())
        if key == 27: #ESC
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
        self.up()
        self.speed(0)
        self.shape('circle')
        self.turtlesize(0.7, 0.7)
        self.color('red')
        self.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)

    def setpos(self):
        self.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)

class Sharp(turtle.Turtle):
    def __init__(self,*args,**kwargs):
        super(Sharp,self).__init__(*args,**kwargs)
        self.up()
        self.speed(0)
        self.shape('sharp')
        self.turtlesize(2, 2)
        self.color('green')

    def setpos(self):
        self.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)