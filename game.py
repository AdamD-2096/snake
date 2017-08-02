from snake import Snake, Food, Sharp
from msvcrt import getch

class Game():

    def __init__(self):
        self.sss = 'sss'
        self.diff = int(input("pick self.difficulty 1:easy 2:normal 3:insane \n"))
        if self.diff == 1:
            self.foodnum = 3
            self.sharpnum = 1
        elif self.diff == 2:
            self.foodnum = 2
            self.sharpnum = 4
        else:
            self.foodnum = 1
            self.sharpnum = 8
        self.ouch = ['s','sh','sha','shar','sharp','sharps','sharpsh','sharpsha','sharpshar','sharpsharp','sharpsharps','sharpsharpsh',]
        self.yum = ['fo','foo','food']

    def comp(self, i,):
        self.ouch[i].setpos()
        for y in range(self.foodnum):
            if self.ouch[i].distance(self.yum[y]) < 30:
                self.comp(i)

    def start(self):
        for i in range(self.foodnum):
            self.yum[i] = Food()
        for i in range(self.sharpnum):
            self.ouch[i] = Sharp()
            self.comp(i)
        print("Snake is hungy! \n BUT")
        print("Watch out for sharp things!!!")

    def restart(self):
        for i in range(self.foodnum):
            self.yum[i].setpos()
        for i in range(self.sharpnum):
            self.comp(i)

    def doublecheck(self, i):
        for y in range(self.sharpnum):
            if self.yum[i].distance(self.ouch[y]) < 30:
                self.yum[i].setpos()
                self.doublecheck(i)
    def alive(self):
        if self.sss.pos in self.sss.pastpos:
            print('gameover')
            self.sss.gameover(1)
            self.restart()
            self.sss.begin()

    def pause(self):
        print("paused")
        print('to exit press esc')
        print("to resume press any key")
        key = ord(getch())
        if key == 27:
            print("EXITED")
            return 27
        print("resumed")
        key = self.sss.getkey()
        if key == 27:
            key = self.pause()

    def play(self):
        self.sss = Snake(self.diff)
        self.sss.border()
        self.sss.wn.register_shape("sharp", ((5,-3), (1,1), (0,5), (-1,1), (-5,-3), (0,-1)))
        self.start()
        self.sss.begin()
        print("to pause press esc")
        while True:
            key = self.sss.getkey()
            if key == 27: #ESC
                key = self.pause()
                if key == 27:
                    break

            self.sss.count += 1
            self.alive()
            self.sss.stamp()
            self.sss.pastpos = self.sss.pastpos + [self.sss.pos[0:]]
            self.sss.setposition(self.sss.pos[0], self.sss.pos[1])
            for i in range(self.foodnum):
                if self.sss.distance(self.yum[i]) < 10:
                    self.sss.total += 2
                    self.yum[i].setpos()
                    self.doublecheck(i)
            for i in range(self.sharpnum):
                if self.sss.distance(self.ouch[i]) < 20:
                    self.sss.gameover(0)
                    self.restart()
                    self.sss.begin()
            if self.sss.count > self.sss.total:
                self.sss.clearstamps(1)
                self.sss.count = self.sss.count - 1
                del self.sss.pastpos[0]
        self.sss.wn.bye()

    
