from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
       self.write(f"Score: {self.score}  ", align= ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game over!", align=ALIGNMENT, font=FONT)

    def scorekeeper(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

