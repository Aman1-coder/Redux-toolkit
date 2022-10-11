# This script will simply create spotify logo

####### Spotify logo ######

from turtle import *
import time
bgcolor('black')
time.sleep(2)
speed('slowest')
begin_fill()
fillcolor("#1DB954")
circle(100)
end_fill()
def location(a,b):
    penup()
    goto(a,b)
    pendown()
def logo(direction, pen, cir):
    rt(direction)
    fd(0)
    pensize(pen)
    pencolor('black')
    circle(cir,60)
location(30,40)
logo(-130,15,90)
location(40,65)
logo(60,18,100)
location(60,95)
logo(60,20,110)
hideturtle()
done()
