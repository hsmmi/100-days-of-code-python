from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, thickness=10, fps=60, paddle_speed=20) -> None:
        super().__init__()
        self.thickness = thickness
        self.paddle_size = thickness
        self.fps = fps
        self.padde_speed = paddle_speed
        self.move_speed = self.thickness * self.padde_speed / self.fps
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=thickness / 2, stretch_len=thickness / 20)
        self.penup()
        self.height = self.screen.window_height()
        self.width = self.screen.window_width()
        self.goto(position)

    def go_up(self):
        new_y = min(
            self.ycor() + self.move_speed,
            self.height / 2 - (self.paddle_size - 3) * self.thickness,
        )
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = max(
            self.ycor() - self.move_speed,
            -self.height / 2 + (self.paddle_size - 3) * self.thickness,
        )
        self.goto(self.xcor(), new_y)

    def go_left(self):
        if self.xcor() > 0:
            new_x = max(self.xcor() - self.move_speed, 2 * self.thickness)
        else:
            new_x = max(
                self.xcor() - self.move_speed,
                -self.width / 2 + 3.5 * self.thickness,
            )
        print(new_x)
        self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 0:
            new_x = min(self.xcor() + self.move_speed, -2 * self.thickness)
        else:
            new_x = min(
                self.xcor() + self.move_speed,
                self.width / 2 - 3.5 * self.thickness,
            )
        self.goto(new_x, self.ycor())

    def shrink(self):
        self.paddle_size = max(self.paddle_size - 1, 4)
        self.shapesize(stretch_wid=self.thickness / 2, stretch_len=self.thickness / 20)

    def grow(self):
        self.paddle_size = min(self.paddle_size + 1, 2 * self.thickness)
        self.shapesize(
            stretch_wid=self.paddle_size / 2, stretch_len=self.thickness / 20
        )
