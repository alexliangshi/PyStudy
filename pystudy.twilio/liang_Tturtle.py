# -*- coding:utf-8 -*-

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.forward(100)
    brad.right(90)
    window.exitonclick()


draw_square()
