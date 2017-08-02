from snake import Snake, Food

class Game():

    def play(self):
        sss = Snake()
        food = Food()
        sss.begin()
        print("to pause press esc")
        while True:
            key = sss.getkey()
            if key == 27: #ESC
                break
            sss.count += 1
            if sss.pos in sss.pastpos:
                print('gameover')
                sss.gameover()
                food.setpos()
                sss.begin()
            sss.stamp()
            sss.pastpos = sss.pastpos + [sss.pos[0:]]
            sss.setposition(sss.pos[0], sss.pos[1])
            if sss.distance(food) < 10:
                sss.total += 2
                food.setpos()
            if sss.count > sss.total:
                sss.clearstamps(1)
                sss.count = sss.count - 1
                del sss.pastpos[0]
        sss.wn.bye()
