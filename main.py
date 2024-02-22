import random
from turtle import *
robot=Turtle()
robot.shape("turtle")
robot.color("red")
robot.fillcolor("white")
colours: list[str] = ["light gray", "medium blue", "cyan", "aquamarine", "medium slate blue", "hot pink"]
def shapes(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        robot.forward(100)
        robot.right(angle)
for shapes_side in range(3, 11):
    robot.color(random.choice(colours))
    shapes(shapes_side)


































screen=Screen()
screen.exitonclick()