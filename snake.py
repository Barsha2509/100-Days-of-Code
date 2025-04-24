from tkinter.constants import RIGHT
from turtle import Turtle
import random
# angle = [0, 90, 180, 360]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.turtles = []
        self.creator()
        self.head = self.turtles[0] #the head of the snake/first segment of the snake
        self.body = self.turtles[1]#middle segment of the snake
        self.tail = self.turtles[-1] #tail of the snake/last segment of the snake
    # def creator(self):
    #     for i in range(0,3):
    #         x = 0
    #         y = 0
    #         tim=Turtle(shape="square")
    #         tim.penup()
    #         tim.color("white")
    #         tim.goto(x=x,y=y)
    #         self.turtles.append(tim)
    #         x =-20

    def creator(self):
        for i in range(0,3):
            x = 0
            y = 0
            # tim=Turtle(shape="square")
            # tim.penup()
            # tim.color("white")
            # tim.goto(x=x,y=y)
            # self.turtles.append(tim)
            self.add_segment(pos1=x,pos2=y)
            x =-20

    def add_segment(self,pos1,pos2):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(x=pos1, y=pos2)
        self.turtles.append(tim)
        # print(self.turtles)

    def extend(self):
        self.add_segment(self.turtles[-1].xcor(),self.turtles[-1].ycor())




    # def right(self):
    #     if self.turtles[0].heading() != LEFT:
    #         for i in self.turtles:
    #             i.left(RIGHT)
    # def up(self):
    #     if self.turtles[0].heading() != DOWN:
    #         for i in self.turtles:
    #             i.left(UP)
    #
    # def left(self):
    #     if self.turtles[0].heading() != RIGHT:
    #         for i in self.turtles:
    #             i.left(LEFT)
    #
    # def down(self):
    #     if self.turtles[0].heading() != UP:
    #         for i in self.turtles:
    #             i.left(DOWN)

    def move(self):
        distance = random.randint(0,20)
        #angle = [0, 90, 180, 360]
        for i in range(len(self.turtles)-1, 0, -1):#start from the end of the list upto the start
            new_x = self.turtles[i-1].xcor()#get the x coordinate of the second last item in the list
            new_y = self.turtles[i-1].ycor()#get the y coordinate of the second last item in the list
            self.turtles[i].goto(new_x,new_y) #move the current item to previous item position
        self.head.forward(distance)#moving first item in the list, 2nd and 3rd don't need to be moved because they will move automatically following above logic
        # self.turtles[0].left(random.choice(angle))


    def right(self):
        if self.head.heading() != LEFT:#So that snake goes forward but not backward
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)





