import another_module

# print(another_module.another_variable) # point at variable

# import turtle
#
# timmy = turtle.Turtle()  # create object named timmy by pointing at Class

from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy) # Turtle object from turtle module
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.speed(1)
# timmy.forward(100)

# my_screen = Screen()  #Class named Screen
# print(my_screen.canvheight)
#
# my_screen.exitonclick()
# ////////////////////////////////
# https://pypi.org/project/prettytable/#description
from prettytable import PrettyTable

table = PrettyTable()
# print(type(table))
# <class 'prettytable.prettytable.PrettyTable'>  >>
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
# table.align["Pokemon Name"] = "r"

table.align = "l"
print(table.align)  #return current setting

print(table)


