import random
from turtle import Turtle


class Food(Turtle):
    """We can create obstacles on the screen"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.penup()
        self.show_on_screen()

    def show_on_screen(self):
        """randomizing position of obstacle(food)"""
        self.x = random.randint(-270, 270)
        self.y = random.randint(-270, 270)
        self.goto(self.x, self.y)
