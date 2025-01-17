from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):  # Corrected __int__ to __init__
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # Use a method to set the initial position of the food

    def refresh(self):  # Add this method to relocate the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
