from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, thickness=10) -> None:
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(
            stretch_wid=thickness / 2, stretch_len=thickness / 20, outline=None
        )
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
