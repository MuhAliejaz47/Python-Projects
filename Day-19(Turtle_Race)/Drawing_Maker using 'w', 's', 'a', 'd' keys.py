from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkeypress(move_forward, 'w')
screen.onkeypress(fun=move_backward,key='s')
screen.onkeypress(fun=move_right,key='d')
screen.onkeypress(fun=move_left,key='a')
screen.onkeypress(fun=clear, key='c')

screen.exitonclick()
