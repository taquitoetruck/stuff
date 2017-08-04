from turtle import * #brings in turtle code
import math #brings in additional math functions

# Name your Turtle.
t = Turtle()
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos,y_pos)
t.pensize(20)
t.penup
### Write your code below:
for trail in range(3):
    t.pendown()
    t.pencolor("salmon")
    t.fd(100)
    t.left(120)
    
# Close window on click.
exitonclick()
