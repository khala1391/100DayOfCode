from turtle import *


# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)


# from turtle import Turtle
# from random import random

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)
#
# print(t.color())    #black, black  pencolor, fillcolor

# t.setheading(0)    # right
# t.setheading(90)   # up
# t.setheading(180)  # left
# t.setheading(270)  # down
# t.screen.mainloop()  # always show screen

def alpha(a, b):
    c = a + b
    print(c)


# https://youtu.be/FJ7iT-0XFQk?si=KhDEv4siI7mWudQH
def beta(a: str, b: int, c):  # just hint, not static
    print(a.upper())
    print(c)


# alpha(2,9)

# point = 1, 7
# print(point[0])
# print(point[1])
#
# print(type(point))  # tuple
#
# pointB = (1,7)
# print(pointB[0])
# print(pointB[1])
#
# print(type(pointB)) # tuple
#
# monsters = ("pikachu", "bulbasaur", "eevee")
# print(monsters[0])

# ///////////////////////////

class Person:
    name = "John"
    age = 36
    country = "Norway"


# print(dir(Person))

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
   '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']
'''


