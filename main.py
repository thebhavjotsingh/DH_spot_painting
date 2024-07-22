"""
Written by: Bhvajot Singh
About:
A simple program for creating Spot paintings like that of Damien Hirst.
"""
import colorgram, random
import turtle as tur

source_img = "pic2.jpg"

colors = colorgram.extract(source_img, 36)
colors_list = []

for c in range(3,len(colors)):
    c_tuple = (colors[c].rgb.r, colors[c].rgb.g, colors[c].rgb.b)
    colors_list.append(c_tuple)
print(len(colors_list))

tur.colormode(255)
cur = tur.Turtle()
cur.speed(0)
cur.penup()
cur.hideturtle()

cur.setheading(225)
cur.forward(300)
cur.setheading(0)

def draw(dots):
    for dot in range(1, dots+1):
        cur.dot(20, random.choice(colors_list))
        cur.forward(50)
        if dot % 10 == 0:
            cur.setheading(90)
            cur.forward(50)
            cur.setheading(180)
            cur.forward(500)
            cur.setheading(0)

draw(100)
screen = tur.Screen()
screen.exitonclick()