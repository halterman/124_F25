import turtle

def star(x: float, y: float) -> None:
    turtle.teleport(x, y)
    for i in range(5):
        turtle.forward(150)
        turtle.right(144)


star(-200, 200)
star(200, -100)

turtle.mainloop()