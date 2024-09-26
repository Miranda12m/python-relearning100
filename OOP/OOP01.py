from turtle import *
import random as rd

# Turtle python library

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('DeepPink4')

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.left(120)
        timmy.forward(50)

        if steps == 5:
            timmy.screen.bgcolor('orange')
            



        print(timmy.pos())
        
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(150)
# timmy.left(120)
# timmy.forward(150)
# timmy.left(120)
# timmy.forward(150)
timmy.home()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
