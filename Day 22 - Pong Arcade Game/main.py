import time
from turtle import Screen
from game_board import GameBoard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


class PongGame:
    def __init__(self, **kwargs):
        self.width = kwargs["width"] if "width" in kwargs else 800
        self.height = kwargs["height"] if "height" in kwargs else 600
        self.thickness = kwargs["thickness"] if "thickness" in kwargs else 10
        self.fps = kwargs["fps"] if "fps" in kwargs else 30
        self.ball_speed = kwargs["ball_speed"] if "ball_speed" in kwargs else 20
        print(self.ball_speed)
        print(self.ball_speed)
        self.paddle_speed = kwargs["paddle_speed"] if "paddle_speed" in kwargs else 40
        self.screen = Screen()
        GameBoard(self.width, self.height, self.thickness)
        self.create_paddle()
        self.ball = Ball(self.thickness, self.fps, self.ball_speed)
        self.scoreboard = Scoreboard(self.width, self.height, self.thickness)
        self.run()

    def create_paddle(self):
        self.r_pos = self.width / 2 - 1.5 * self.thickness
        self.l_pos = -self.width / 2 + 1.5 * self.thickness
        self.r_paddle = Paddle(
            (self.r_pos, 0), self.thickness, self.fps, self.paddle_speed
        )
        self.l_paddle = Paddle(
            (self.l_pos, 0), self.thickness, self.fps, self.paddle_speed
        )

        self.screen.listen()

        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.r_paddle.go_left, "Left")
        self.screen.onkey(self.r_paddle.go_right, "Right")

        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")
        self.screen.onkey(self.l_paddle.go_left, "a")
        self.screen.onkey(self.l_paddle.go_right, "d")

    def run(self):
        a = 1
        while True:
            print(a)
            a += 1
            for _ in range(self.fps):
                time.sleep(1 / self.fps)
                self.ball.move()
                # self.screen.onkey(self.ball.move, "space")
                self.check_collision()
                self.check_paddle_collision()
                self.check_miss()
                self.screen.update()

    def check_collision(self):
        if (
            self.ball.ycor() > self.height / 2 - 1 * self.thickness
            or self.ball.ycor() < -self.height / 2 + 1 * self.thickness
        ):
            self.ball.bounce_y()

    def check_paddle_collision(self):
        print(self.ball.distance(self.r_paddle))
        print(self.ball.distance(self.l_paddle))
        if (
            self.ball.distance(self.r_paddle)
            < (self.r_paddle.paddle_size + 1) / 2 * self.thickness
            and self.ball.xcor() > self.r_paddle.xcor() - 2 * self.thickness
        ) or (
            self.ball.distance(self.l_paddle)
            < (self.l_paddle.paddle_size + 1) / 2 * self.thickness
            and self.ball.xcor() < self.l_paddle.xcor() + 2 * self.thickness
        ):
            self.ball.bounce_x()

    def check_miss(self):
        if self.ball.xcor() > self.r_paddle.xcor():
            self.scoreboard.l_goal()
            self.l_paddle.shrink()
            self.r_paddle.grow()
            self.ball.reset_position()
        elif self.ball.xcor() < self.l_paddle.xcor():
            self.scoreboard.r_goal()
            self.r_paddle.shrink()
            self.l_paddle.grow()
            self.ball.reset_position()


game_settings = {
    "width": 1000,
    "height": 600,
    "thickness": 10,
    "fps": 20,
    "ball_speed": 10,
    "paddle_speed": 50,
}
my_game = PongGame(**game_settings)
