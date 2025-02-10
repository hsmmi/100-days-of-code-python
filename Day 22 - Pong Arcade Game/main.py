import time
from turtle import Screen
from game_board import GameBoard
from paddle import Paddle
from turtle import Turtle
from ball import Ball
from scoreboard import Scoreboard


class PongGame:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.thickness = 10
        self.screen = Screen()
        GameBoard(self.width, self.height, self.thickness)
        self.create_paddle()
        self.ball = Ball()
        self.scoreboard = Scoreboard(self.width, self.height, self.thickness)
        self.run()

    def create_paddle(self):
        self.r_pos = self.width / 2 - 3.5 * self.thickness
        self.l_pos = -self.width / 2 + 2.5 * self.thickness
        self.r_paddle = Paddle((self.r_pos, 0))
        self.l_paddle = Paddle((self.l_pos, 0))
        self.screen.listen()
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")

    def run(self):
        while True:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()
            self.check_collision()
            self.check_paddle_collision()
            self.check_miss()

    def check_collision(self):
        if (
            self.ball.ycor() > self.height / 2 - 2 * self.thickness
            or self.ball.ycor() < -self.height / 2 + 3 * self.thickness
        ):
            self.ball.bounce_y()

    def check_paddle_collision(self):
        if (
            self.ball.distance(self.r_paddle) < 6 * self.thickness
            and self.ball.xcor() > self.r_pos - 2 * self.thickness
        ) or (
            self.ball.distance(self.l_paddle) < 6 * self.thickness
            and self.ball.xcor() < self.l_pos + self.thickness
        ):
            self.ball.bounce_x()

    def check_miss(self):
        if self.ball.xcor() > self.r_pos - self.thickness:
            self.ball.reset_position()
            self.scoreboard.r_miss()
        elif self.ball.xcor() < self.l_pos:
            self.ball.reset_position()
            self.scoreboard.l_miss()

    def game_over(self):
        self.screen.mainloop()


my_game = PongGame()
