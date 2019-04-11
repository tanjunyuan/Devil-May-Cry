import turtle
import random
turtle.speed('slowest')
turtle.pensize(9)
x=0
y=0
colors=['red','blue','yellow','black','green','pink','gray','purple','orange']
for i in range(1,1000):
    e=random.randint(1,5)
    m=random.randint(0,8)
    turtle.pencolor(colors[m])
    if e==1:
        x+=1
    elif e==2:
        x-=1
    elif e==3:
        y+=1
    elif e==4:
        y-=1
    else:
        turtle.circle(x*10)
    turtle.goto(x*10,y*10)
