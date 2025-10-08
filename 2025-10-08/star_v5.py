import turtle
import random

turtle.tracer(0)
turtle.hideturtle()

colors = ['red', 'green', 'blue', 'black', 'purple']

def star(x: float, y: float, size: float, color: str) -> None:
    turtle.teleport(x, y)
    turtle.color(color)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def click(x: float, y: float) -> None:
    star(x, y, 50, 'blue')
    print(f'\ax = {x}, y = {y}')
    turtle.update()

# star(-200, 200, 200, 'red')
# star(200, -100, 75, 'blue')

# Draw a bunch of stars
for i in range(10):
    x = random.randrange(-400, 400)
    y = random.randrange(-400, 400)
    s = random.randrange(5, 150)
    star(x, y, s, random.choice(colors))

turtle.onscreenclick(click)

turtle.update()
turtle.mainloop()