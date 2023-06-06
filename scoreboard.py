from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0,y=250)
        self.hideturtle()
        self.scoreadd()

    def scoreadd(self):
        self.write(align="center", font=FONT, arg=f"Score: {self.score}")

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.scoreadd()

    def gameover(self):
        self.goto(0,0)
        self.write(align="center", font=FONT, arg=f"Game Over")