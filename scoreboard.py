from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 10, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highest_score.txt") as file:
            self.highest_score = int(file.read())
        self.hideturtle()
        self.score = 0
        self.color("white")

    def score_board(self):
        self.penup()
        self.clear()
        self.goto(0, 280)
        self.write(f"Score:{self.score}  Highest Score:{self.highest_score}", align=ALIGNMENT,font=FONT)

    def increment(self):
        self.score += 1


    def high_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0


