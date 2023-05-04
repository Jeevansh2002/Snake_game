from turtle import *


POSITIONS = [(0,0), (-20,0), (-40,0)]
FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()


    def create_snake(self):
        for i in POSITIONS:
            cherry = Turtle("square")
            cherry.penup()
            cherry.goto(i)
            cherry.color("white")
            self.snakes.append(cherry)

    def move_snake(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].fd(FORWARD)



    def creating_snake(self):
        for i in POSITIONS:
            self.add_snake(i)


    def add_snake(self, i):
        cherry = Turtle("square")
        cherry.penup()
        cherry.goto(i)
        cherry.color("white")
        self.snakes.append(cherry)

    def new_snake(self):
        for i in self.snakes:
            i.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()

    def goto(self):
        self.add_snake(self.snakes[-1].position())


    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != LEFT:
           self.snakes[0].setheading(0)




