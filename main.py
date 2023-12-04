import secrets
import time

from turtle import Turtle, Screen

from snake import Snake

from score_board import Score_Board
from score_board import BEST_SCORE_FILE

from food import Food


"""Setting up the screen settings"""
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


sname = screen.textinput(
    "THE SNAKE GAME", "Welcome into The Snake Game. Enter your name.").capitalize()


def game_on():
    global sname
    global screen

    snake1 = Snake()
    obstacle = Food()

    def next_round():
        """It is bound to spacebar, we can start new game"""
        screen.reset()
        game_on()

    """binding key functions"""
    screen.listen()
    screen.onkey(snake1.up, "Up")
    screen.onkey(snake1.down, "Down")
    screen.onkey(snake1.right, "Right")
    screen.onkey(snake1.left, "Left")
    screen.onkey(snake1.up, "w")
    screen.onkey(snake1.down, "s")
    screen.onkey(snake1.right, "d")
    screen.onkey(snake1.left, "a")
    screen.onkey(screen.bye, "Escape")

    board = Score_Board(sname)

    board.counting()

    game_is_on = True
    sec = 0.1

    """Loop below sets our snake in motion"""
    while game_is_on:
        """Snake delay"""
        time.sleep(sec)

        board.give_score()
        snake1.move()
        screen.update()

        """'If' statement below represent action when snake hits an obstacle(food)"""
        if (obstacle.distance(snake1.segments[0])) < 17:

            obstacle.show_on_screen()
            snake1.segments.append(Turtle("square", visible=False))
            board.score += 1
            board.give_score()
            snake1.create_snake()

            """Speeding up our snake if score reaches higher value, but with maximum speed restriction"""
            if sec > 0.025:
                sec = sec - 0.01 * (board.score/100)
            else:
                sec = 0.025

        """'If' statement below represent action when snake hits a side wall"""
        if snake1.segments[0].xcor() >= 280 or snake1.segments[0].xcor() <= -281:
            game_is_on = False
            screen.reset()
            board.color("white")
            board.game_over()
            screen.onkey(next_round, "space")

        """'If' statement below represent action when snake hits floor or ceiling"""
        if snake1.segments[0].ycor() >= 281 or snake1.segments[0].ycor() <= -280:
            game_is_on = False
            screen.reset()
            board.color("white")
            board.game_over()
            screen.onkey(next_round, "space")

        """Detect collision with own tail"""
        for segment in snake1.segments[1:]:
            if snake1.segments[0].distance(segment) < 10:
                game_is_on = False
                screen.reset()
                board.color("white")
                board.game_over()
                screen.onkey(next_round, "space")

    screen.exitonclick()


game_on()
