import turtle as t_module
import random

#import colorgram
#
# colors = colorgram.extract("hirst-paint_art.jpg", 30)
# rgb_colors = []
#
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    colors_list = (r, g, b)
#    rgb_colors.append(colors_list)
#
#
# print(rgb_colors)
t_module.colormode(255)
tur = t_module.Turtle()
list_of_colors = [(211, 154, 98), (241, 248, 246), (236, 241, 245), (53, 107, 131), (177, 78, 34), (199, 142, 34), (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130), (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), (51, 126, 121), (197, 124, 143), (166, 21, 31), (222, 93, 79), (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), (161, 26, 23), (19, 79, 92), (233, 167, 172), (175, 207, 187), (101, 127, 158), (165, 203, 210)]

tur.penup()
tur.hideturtle()
tur.speed("fastest")
tur.setheading(225)
tur.forward(250)
tur.setheading(0)
num_of_dots = 101

for spot_count in range(1, num_of_dots):
    tur.dot(18, random.choice(list_of_colors))
    tur.forward(50)

    if spot_count % 10 == 0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)






tur = t_module.Screen()
tur.exitonclick()



