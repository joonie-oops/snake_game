from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 260)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def end(self):
        self.clear()
        self.penup()
        self.setpos(0, 0)
        self.color("yellow")
        self.write(f"Game Over! Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
