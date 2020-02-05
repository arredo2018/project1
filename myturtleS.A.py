import turtle
import random


screen = turtle.Screen()
titi = turtle.Turtle()
itit = turtle.Turtle()
tttt = turtle.Turtle()
iiii = turtle.Turtle()
tttt.shape("classic")
iiii.shape("classic")
titi.shape("classic")
itit.shape("classic")
A = random.randrange(1000)
B = random.randrange(1000)



iiii.begin_fill()
iiii.color("black" , "green")
iiii.forward(200)
iiii.left(50)
iiii.forward(150)
iiii.circle(80)
iiii.left(90)
iiii.forward(150)
iiii.left(50)
iiii.forward(150)
iiii.circle(80)
iiii.end_fill()

tttt.begin_fill()
tttt.color("black" , "yellow")
tttt.backward(200)
tttt.right(50)
tttt.backward(150)
tttt.circle(80)
tttt.right(90)
tttt.backward(150)
tttt.right(50)
tttt.backward(150)
tttt.circle(80)
tttt.end_fill()


itit.begin_fill()
itit.color("black" , "red")
itit.forward(200)
itit.left(-50)
itit.forward(150)
itit.circle(-80)
itit.left(-90)
itit.forward(150)
itit.left(-50)
itit.forward(150)
itit.circle(-80)
itit.end_fill()


titi.begin_fill()
titi.color("black" , "blue")
titi.backward(200)
titi.right(-50)
titi.backward(150)
titi.circle(-80)
titi.right(-90)
titi.backward(150)
titi.right(-50)
titi.backward(150)
titi.circle(-80)
titi.end_fill()


screen.mainloop()