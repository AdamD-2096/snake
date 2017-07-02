import turtle
from random import randrange
from msvcrt import getch, kbhit

wn = turtle.Screen()
sss = turtle.Turtle()

sss.up()
sss.speed(0)
sss.shape('circle')
pos = [0, 0]
count = 0
total = 5

def changepos(dirc, neg):
    if dirc == 'X':
        if neg == '-':
            pos[0] += -5
        else:
            pos[0] += 5

    if dirc == 'Y':
        if neg == '-':
            pos[1] += -5
        else:
            pos[1] += 5

def getkey():
    while kbhit() == 0:
        pass
    key = ord(getch())
    if key == 27: #ESC
        return 27
    elif key == 80: #Down arrow
        changepos('Y', '-')
    elif key == 72: #Up arrow
        changepos('Y', '+')
    elif key == 75: #Left arrow
        changepos('X', '-')
    elif key == 77: #Right arrow
        changepos('X', '+')
    else:
        getkey()

while True:
    key = getkey()
    if key == 27: #ESC
        break
    count += 1
    
    sss.stamp()
    sss.setposition(pos[0], pos[1])
    if count > total:
        sss.clearstamps(1)
        count = count - 1
    

wn.exitonclick()