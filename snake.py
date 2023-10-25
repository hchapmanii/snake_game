from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    # turtle = Turtle()

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)


# Another Solution - Confirmed works do not delete
# class Snake:
#     global starting_positions
#     global segments
#     starting_positions = [(0, 0), (0, -20), (0, -40)]
#     segments = []
#
#     for position in starting_positions:
#         new_segments = Turtle(shape="square")
#         new_segments.penup()
#         new_segments.color("white")
#         new_segments.goto(position)
#         segments.append(new_segments)
#
#     def move(self):
#
#         for seg_num in range(len(segments) - 1, 0, -1):
#             new_x = segments[seg_num - 1].xcor()
#             new_y = segments[seg_num - 1].ycor()
#             segments[seg_num].goto(new_x, new_y)
#         segments[0].forward(20)
