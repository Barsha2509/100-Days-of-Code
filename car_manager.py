from turtle import Turtle
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
y = list(range(-250, 250))
move_distance = 10

class Cars:


    def __init__(self):
        self.cars = []
        self.car_speed = move_distance


    def car_maker(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(colors))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.choice(y))
            self.cars.append(new_car)


    def move(self):
        for i in self.cars:
            i.backward(self.car_speed)

    def speedup(self):
        self.car_speed += move_distance




