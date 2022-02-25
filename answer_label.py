from turtle import Turtle


class AnswerLabel(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def create_label(self, answer, x, y):
        self.goto(x, y)
        self.write(answer, False, align="center")
