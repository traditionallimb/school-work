from turtle import Turtle
from random import randint

tu = Turtle()
rt = Turtle()
le = Turtle()
tu.color('red')
rt.color('blue')
le.color('green')
tu.shape('turtle')
rt.shape('turtle')
le.shape('turtle')


tu.penup()
tu.goto(-160, 100)
tu.pendown()
rt.penup()
rt.goto(-160, 70)
rt.pendown()
le.penup()
le.goto(-160, 40)
le.pendown()

for movement in range(100):
    tu.forward(randint(1, 5))
    rt.forward(randint(1, 5))
    le.forward(randint(1, 5))

input("Press enter to close")
