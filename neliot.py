import turtle

def piirra_nelio(sivu, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    if x < 0:
        turtle.fillcolor("red")
    else:
        turtle.fillcolor("blue")
    
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(sivu)
        turtle.right(90)
    turtle.end_fill()
    
piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
turtle.done()
