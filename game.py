from snake import Snake, Food, Sharp

class Game():

    def __init__(self):
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

    def play(self):
        sss = Snake(self.diff)
        sss.border()
        sss.wn.register_shape("sharp", ((5,-3), (1,1), (0,5), (-1,1), (-5,-3), (0,-1)))
        self.start()
        sss.begin()
        print("to pause press esc")
        while True:
            key = sss.getkey()
            if key == 27: #ESC
                break
            sss.count += 1
            if sss.pos in sss.pastpos:
                print('gameover')
                sss.gameover(1)
                self.restart()
                sss.begin()
            sss.stamp()
            sss.pastpos = sss.pastpos + [sss.pos[0:]]
            sss.setposition(sss.pos[0], sss.pos[1])
            for i in range(self.foodnum):
                if sss.distance(self.yum[i]) < 10:
                    sss.total += 2
                    self.yum[i].setpos()
                    self.doublecheck(i)
            for i in range(self.sharpnum):
                if sss.distance(self.ouch[i]) < 20:
                    sss.gameover(0)
                    self.restart()
                    sss.begin()
            if sss.count > sss.total:
                sss.clearstamps(1)
                sss.count = sss.count - 1
                del sss.pastpos[0]
        sss.wn.bye()

    
