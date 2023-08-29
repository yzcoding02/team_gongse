import turtle as t

def equilateralTriangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(3):
        t.forward(75)
        t.left(120)
    t.penup()
    t.goto(0, 0)

def square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.penup()
    t.goto(0, 0)

t.speed(0)
t.shape("turtle")
t.onscreenclick(equilateralTriangle)
t.onscreenclick(square, 3)

t.mainloop()