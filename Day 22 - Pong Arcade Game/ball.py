from turtle import Turtle


class Ball(Turtle):
    def __init__(self, thickness=10, fps=60, ball_speed=20) -> None:
        super().__init__()
        self.fps = fps
        self.thickness = thickness
        self.ball_speed = ball_speed
        print(self.ball_speed)
        self.move_speed = self.ball_speed / self.fps
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=thickness / 10, stretch_len=thickness / 10)
        self.penup()
        self.x_move = thickness
        self.y_move = thickness

    def move(self):
        new_x = self.xcor() + self.x_move * self.move_speed
        new_y = self.ycor() + self.y_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1.1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = self.ball_speed / self.fps
        self.bounce_x()
        self.bounce_y()
