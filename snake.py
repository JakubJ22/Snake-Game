from turtle import Turtle



class Snake:

    def __init__(self):
        """Creating a segments of snake which be linked in next function"""
        self.amount = 3

        self.extend_snake()
        self.create_snake()

    def create_snake(self):
        """Creating a snake from segments which are 'smaller' objects"""
        for segment in self.segments:
            segment.color("white")
            segment.penup()
            segment.showturtle()

        self.segments[0].color("red")

    def extend_snake(self):

        self.segments = [Turtle("square", visible=False)
                         for _ in range(self.amount)]
        self.amount += 1

    def move(self):
        """Putting each segment of snake into a possition of previous one"""
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].speed("fastest")
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
