import turtle as t

def one():
    t.circle(25)
def two():
    t.circle(50)
def three():
    t.circle(100)
def four():
    t.circle(150)
def colorChangeGoto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def clear():
    t.clear()
def red():
    t.color("red")
def black():
    t.color("black")
def brown():
    t.color("brown")
t.onkey(one,"1")
t.onkey(two,"2")
t.onkey(three,"3")
t.onkey(four,"4")
t.onkey(clear,"c")
t.onkey(red,"r")
t.onkey(black,"b")
t.onkey(brown,"B")
t.onscreenclick(colorChangeGoto)
t.shape("turtle")
t.listen()
t.speed(0)






t.mainloop()