from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.penup()
        self.rand_position()

    def rand_position(self):
        x_coord = random.randint(-280, 280)
        y_coord = random.randint(-280, 280)
        self.setpos(x_coord, y_coord)
