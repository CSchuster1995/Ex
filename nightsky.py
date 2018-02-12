import random
from turtle import *

stars = random.randrange(25, 50)
bgcolor('black')
color('yellow', "yellow")



for i in range(stars):
    random.randx = random.randrange(-290,290)
    random.randy = random.randrange(-290, 291)
    penup()
    goto(ranx, randy)
    star = range(5, 25)
    begin_fill()
    for i in range(5):
        forward(star)
        right(144)
    end_fill()
    penup()


mainloop()





       




mainloop()