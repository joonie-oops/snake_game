from turtle import Turtle
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        first_segment = Turtle("square")
        first_segment.color("white")
        first_segment.penup()
        self.head = first_segment
        self.segments = [first_segment]
        self.extend()
        self.extend()

    def extend(self):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.setpos(self.segments[-1].pos())
        self.segments.append(seg)

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[idx - 1].xcor()
            new_y = self.segments[idx - 1].ycor()
            self.segments[idx].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_eat_self(self):
        for body_seg in self.segments[1:]:
            if self.head.distance(body_seg) <= 10:
                return True

        return False




