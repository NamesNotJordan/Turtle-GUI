from turtle import Turtle, Screen

raph = Turtle()
raph.shape("turtle")
raph.color("red")


# Challenge 2
for i in range(10):
    raph.down()
    raph.forward(10)
    raph.up()
    raph.forward(10)
    
# Challenge 3
def draw_polygon(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        raph.forward(100)
        raph.right(angle)



screen = Screen()