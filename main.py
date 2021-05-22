import turtle
import time
t = turtle.Turtle()
t.screen.bgcolor("pink")
t.color('red')
t.speed(10)
# Outer circle
x = 0
y = -200
t.penup()
t.goto(x, y)
t.begin_fill()
t.fillcolor('light blue')
t.pendown()
t.circle(200)
t.end_fill()
t.hideturtle()

# Inner cirlce
y = -100
t.penup()
t.goto(x, y)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.circle(100)
t.end_fill()

t.penup()
t.home()
t.left(90)
for i in range(12):
    t.right(360/12)
    t.forward(150)
    t.pendown()
    t.write(i+1)
    t.penup()
    t.goto(0, 0)



hour = turtle.Turtle()
minute = turtle.Turtle()
second = turtle.Turtle()

hour.hideturtle()
minute.hideturtle()
second.hideturtle()

dot = turtle.Turtle()

minute.left(90)
dot.speed(0)
i = 1
dot.left(90)
angle = 360/60

while i <= 60:

    dot.penup()
    dot.right(angle)
    dot.forward(155)
    dot.begin_fill()
    dot.fillcolor('black')
    dot.pendown()
    if i % 5 != 0:
        dot.circle(2)
    dot.end_fill()
    i = i+1
    dot.penup()
    dot.goto(0, 0)

dot.hideturtle()
minutes = 0
hour.left(180)
def hour_hand(angle=None):
    hour.hideturtle()
    if angle == None:
        hour.pensize(5)
        hour.forward(90)
        hour.hideturtle()
        hour.penup()
        hour.goto(0, 0)
        hour.pendown()

    else:
        hour.clear()
        hour.pensize(5)
        hour.right(30)
        hour.pensize(5)
        hour.forward(90)
        hour.penup()
        hour.goto(0, 0)
        hour.pendown()


def minute_hand(angle=None):
    global minutes
    if angle == None:
        minute.pensize(3)
        minute.forward(120)
        minute.hideturtle()
        minute.penup()
        minute.goto(0, 0)
        minute.pendown()

    else:
        minute.clear()
        minute.pensize(3)
        minute.right(6)
        minute.pensize(3)
        minute.forward(120)
        minute.penup()
        minute.goto(0, 0)
        minute.pendown()
        minutes=minutes+1
    if minutes==60:
        minutes=0
        hour_hand(30)

second.left(90)


def second_hand():

    a = 360/60
    second.right(a)
    second.pensize(2)
    second.forward(140)
    second.undo()
    second.clear()
    # second.goto(0, 0)


hour_hand()
minute_hand()

seconds = 0
while True:
    if seconds == 60:
        seconds = 0
        minute_hand(angle)
    start_time = time.time()
    time.sleep(1-(time.time()-start_time))
    second_hand()
    seconds = seconds+1

turtle.done()
