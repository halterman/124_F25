import turtle

turtle.tracer(0)
turtle.hideturtle()

def star(x: float, y: float, size: float, color: str) -> None:
    turtle.teleport(x, y)
    turtle.color(color)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)


star(-200, 200, 200, 'red')
star(200, -100, 75, 'blue')

turtle.update()
turtle.mainloop()