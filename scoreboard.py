from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210, 270)
        self.update_level()


    def update_level(self):
        self.write(f"Level: {self.current_level}", align="Center", font=("Courier", 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=("Courier", 30, "normal"))

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.update_level()

