from turtle import Turtle
import time
FONT = ('Arial', 15, 'normal')


class Score_Board(Turtle):
    """An object of this class shows a score of our game on upper part of the screen"""

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        

    def give_score(self):
        self.clear()
        self.write(f"{self.name}'s Score: {self.score}", align="center",
                   font=FONT)

    def counting(self):
        self.goto(0, 0)
        for number in range(3, 0, -1):
            self.write(f"{number}", align="center",
                       font=FONT)
            time.sleep(0.7)
            self.clear()

        self.goto(0, 280)

    def exit_info(self):
        self.goto(0, -18)
        self.write("Click on the screen to exit", align="center",
                   font=('Arial', 7, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center",
                   font=FONT)
        self.exit_info()
