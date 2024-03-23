#!/usr/bin/python3
""" A pytonic implementation of python
to make a robot"""


class Robot:

    """ A class robot
    that does as instructed"""

    population = 0

    def __init__(self, name):
        """ Initialization of the class
        it only has two properties"""

        self.name = name

        print("(Initializing {})".format(self.name))
        print("_____________________________________")
        print("Hello\nMy name is {}".format(self.name))

        Robot.population += 1

    def do_math(self, x, y):
        """ a module that does simple maths """

        self.x = x
        self.y = y
        print("The addition of {} + {} = {}".format(x, y, x + y))


robotics1 = Robot("C3P0")
robotics1.do_math(45, 6)
print()
robotics2 = Robot("R2D2")
robotics2.do_math(70, 2)
