from turtle import Turtle
NUMBER_OF_SEGMENTS = 3
MOVE_CONSTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(NUMBER_OF_SEGMENTS):
            new_seg = Turtle(shape="circle")
            new_seg.color("yellow")
            new_seg.penup()
            new_seg.goto(-MOVE_CONSTANT * _, 0)
            self.segments.append(new_seg)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            # print(i , snake[i-1].pos())
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(MOVE_CONSTANT)

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

    def add_segment(self):
        new_seg = Turtle(shape="circle")
        new_seg.color("yellow")
        new_seg.penup()
        new_seg.goto(-MOVE_CONSTANT * len(self.segments)-1, 0)
        self.segments.append(new_seg)