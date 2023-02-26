from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-220, 250)
        self.write(f"Level: {self.score}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, "center", FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" GAME OVER\nFINAL SCORE: {self.score}", False, "center", ("courier", 30, "normal"))
