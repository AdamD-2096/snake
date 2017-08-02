import turtle
from random import randrange

class Snake(turtle.Turtle):
    """My Snake turtle"""
    def __init__(self,*args,**kwargs):
        super(Snake,self).__init__(*args,**kwargs)
        print("Time for my turtle snake!")
        self.up()
        self.speed(0)
        self.shape('circle')

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