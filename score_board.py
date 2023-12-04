from turtle import Turtle
import time


FONT = ('Arial', 15, 'normal')

BEST_SCORE_FILE = "best_score.txt"


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
        self.max_score = self.what_is_max_score()

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
        self.write("Click Space to start a new game or Esc to close the window.", align="center",
                   font=('Arial', 9, 'normal'))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center",
                   font=FONT)
        self.exit_info()
        self.update_best_score()
        self.give_best_score()

    def update_best_score(self):
        if self.score > int(self.max_score):
            self.max_score = self.score

            with open(BEST_SCORE_FILE, "w") as file:
                file.write(str(self.max_score))

    def give_best_score(self):
        self.goto(-20, -40)
        self.write(f"Best score: {self.max_score}")

    def what_is_max_score(self):
        try:
            with open(BEST_SCORE_FILE, "r") as file:
                data = file.read()
                if data != '':
                    return int(data)
                else:
                    return int('0')
        except FileNotFoundError:
            file = open(BEST_SCORE_FILE, 'x')
            file.close()