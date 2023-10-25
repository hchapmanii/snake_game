from turtle import Turtle, Screen
from food import Food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write("Scoreboard : ", True, align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=('Arial', 14, 'normal'))

    def score_counter(self, score_count):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Scoreboard: {score_count}", True, align="center", font=('Arial', 14, 'normal'))




