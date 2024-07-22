import colorgram, random
import turtle as tur

source_img = "damian hirst dots.jpg"

colors = colorgram.extract(source_img, 30)
colors_list = []

for c in range(1,len(colors)):
    c_tuple = (colors[c].rgb.r, colors[c].rgb.g, colors[c].rgb.b)
    colors_list.append(c_tuple)

tur.colormode(255)
cur = tur.Turtle()

cur.dot(20, random.choice(colors_list))

screen = tur.Screen()
screen.exitonclick()