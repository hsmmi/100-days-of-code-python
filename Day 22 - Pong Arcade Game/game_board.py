from turtle import Turtle, Screen


class GameBoard(Turtle):
    def __init__(self, width, height, thickness) -> Screen:
        super().__init__()
        self.width = width
        self.height = height
        self.thickness = thickness
        self.screen.setup(
            width=self.width + 4 * self.thickness,
            height=self.height + 4 * self.thickness,
        )
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.draw_border()
        self.draw_center_line()

    def draw_border(self):
        border = Turtle()
        border.speed(0)
        border.color("blue")
        border.width(self.thickness)
        border.hideturtle()
        border.penup()
        border.goto(
            -self.width / 2 - 0.5 * self.thickness,
            self.height / 2 + 0.5 * self.thickness,
        )
        border.pendown()
        for _ in range(2):
            border.forward(self.width + self.thickness)
            border.right(90)
            border.forward(self.height + self.thickness)
            border.right(90)

    def draw_center_line(self):
        center_line = Turtle()
        center_line.speed(0)
        center_line.color("blue")
        center_line.width(self.thickness)
        center_line.hideturtle()
        center_line.penup()
        center_line.goto(0, self.height / 2 - 2 * self.thickness)
        center_line.pendown()
        center_line.setheading(270)
        for _ in range(0, self.height, self.thickness * 6):
            center_line.forward(self.thickness * 2)
            center_line.penup()
            center_line.forward(self.thickness * 4)
            center_line.pendown()
