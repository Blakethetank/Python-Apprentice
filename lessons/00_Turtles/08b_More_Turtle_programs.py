"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle
turtle.setup (width=600, height=600)

tina = turtle.Turtle()

tina.shape('turtle')
tina.speed(3)

tina.pencolor('green')
tina.forward(120)
tina.left(50)
tina.forward(100)
tina.left(40)
tina.forward(120)
tina.left(50)
tina.forward(100)
tina.left(40)
tina.forward(115)












turtle.exitonclick()