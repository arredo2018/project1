import turtle

screen = turtle.Screen()
top = turtle.Turtle()
top.shape("classic")
pop = turtle.Turtle()
pop.shape("classic")
do = turtle.Turtle()
do.shape("classic")
re = turtle.Turtle()
re.shape("classic")

pop.speed(50)
pop.penup()
pop.begin_fill()
pop.goto(125,-290)
pop.pendown()
pop.color("blue" , "black")
pop.begin_fill()
for i in range(50):
    pop.left(90)
    pop.forward(100)
    pop.left(135)
    pop.forward(142)
    pop.left(145)
    pop.forward(152)
pop.end_fill()

re.speed(100)
re.color("red","red")
for i in range(75):
    re.circle(160)
    re.left(5)

top.speed(100)
top.color("purple","purple")
for i in range(75):
    top.circle(80)
    top.left(5)

do.speed(100)
do.goto(-100,-85)
do.color("green" , "green")
for i in range(75):
    do.forward(200)
    do.left(95)


screen.mainloop()