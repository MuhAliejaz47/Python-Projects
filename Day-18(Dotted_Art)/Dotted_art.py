from turtle import Turtle, Screen
import random

def create_grid_of_dots(turtle, grid_size, dot_size, color_list):
    for y in range(grid_size):
        for x in range(grid_size):
            turtle.penup()
            turtle.goto(x * 30, y * 30)
            c = random.choice(color_list)
            turtle.pencolor(c)
            turtle.dot(dot_size)
            

tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39), (131, 37, 27), (45, 73, 76), (219, 177, 170), (24, 43, 43), (49, 88, 21)]

tim.speed('fastest')
tim.pensize(5)
dot_size = 15
grid_size = 10
tim.hideturtle()

create_grid_of_dots(tim, grid_size, dot_size, color_list)

screen.exitonclick()
