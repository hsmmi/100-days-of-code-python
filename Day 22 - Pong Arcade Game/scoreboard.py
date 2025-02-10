from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, width, height, thickness):
        super().__init__()
        self.width = width
        self.height = height
        self.thickness = thickness
        self.color("red")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-5 * self.thickness, self.height / 2 - 5 * self.thickness)
        self.write(
            self.l_score,
            align="center",
            font=("Times New Roman", 3 * self.thickness, "normal"),
        )
        self.goto(+5 * self.thickness, self.height / 2 - 5 * self.thickness)
        self.write(
            self.r_score,
            align="center",
            font=("Times New Roman", 3 * self.thickness, "normal"),
        )

    def r_miss(self):
        self.l_score += 1
        self.update_scoreboard()

    def l_miss(self):
        self.r_score += 1
        self.update_scoreboard()
