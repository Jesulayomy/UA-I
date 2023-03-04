""" A class that defines a person as an object """

from quirks import *
import random
from roles import *


class Person:
    """ defines a base class for people """

    __population = 0

    def __init__(self, name):
        """ Initialization """

        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        self.name = name
        Person.__population += 1

        """ sets a role for the person """
        self.role = role()

        """ assigns a quirk to a user """
        factor = random.randint(0, len(quirk_list))
        self.quirk = quirk_list.pop(factor)

    def intro(self):
        """ introduces a character """

        print(f"Name: {self.name}\nQuirk: {self.quirk}\nStatus: {self.role}")

    @staticmethod
    def population():
        """ Prints the total number of people in the session """

        print(f"There are {Person._Person__population} people in the world")



"""
Types:
    Emitter
    Transform
    Mutation
    Enhancement
"""
