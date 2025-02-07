import turtle as t
import turtle as t
t.setup(800,600,0,0)
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.circle(100,90)
    t.circle(-100,90)
t.circle(100,90/2)
t.fd(100)
t.circle(20,90)