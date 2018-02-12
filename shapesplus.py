from turtle import *

def polygon(n, x, c, d):
    color(c, d)
    begin_fill()
    for i in range(n):
        forward(x)
        right(360/n)
    end_fill()

def star (c):
    color(c)
    for i in range(5):
        forward(100)
        right(144)