from turtle import *
from shapes import *

def star ():
    for i in range(5):
        forward(100)
        right(144)

# Triangle
polygon(3, 100)

# Square
polygon(4, 100)

# Pentagon
polygon(5, 100)

# Hexagon
polygon(6, 100)

# Octagon
polygon(8, 100)

# Star
star() 

# Circle
polygon(360, 1)



mainloop()