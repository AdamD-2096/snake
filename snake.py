import turtle
from random import randrange
from msvcrt import getch, kbhit

wn = turtle.Screen()

sss = turtle.Turtle()
sss.up()
sss.speed(0)
sss.shape('circle')

food = turtle.Turtle()
food.up()
food.speed(0)
food.shape('circle')
food.turtlesize(0.7, 0.7)
food.color('red')
pos = [0, 0]
count = 0
total = 3
food.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)
pastpos = []

def changepos(dirc, neg):
    if dirc == 'X':
        if neg == '-':
            pos[0] += -10
        else:
            pos[0] += 10

    if dirc == 'Y':
        if neg == '-':
            pos[1] += -10
        else:
            pos[1] += 10

def pause():
    while True:
        while kbhit() == 0:
            pass
        key = ord(getch())
        if key == 27:
            return 27
        if key == 13: #enter
            break
    

def getkey():
    while kbhit() == 0:
        pass
    key = ord(getch())
    if key == 27: #ESC
        key = pause()
        if key == 27:
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
    if sss.distance(food) < 10:
        total += 2
        food.setposition(randrange(-20, 20) * 10, randrange(-20, 20) * 10)
    if count > total:
        sss.clearstamps(1)
        count = count - 1
    

wn.bye()