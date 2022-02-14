from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("log.txt") as log:
            self.high_score = int(log.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("log.txt", mode="w") as log:
                log.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
