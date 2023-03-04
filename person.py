""" A class that defines a person as an object """

from quirks import *
import random
from roles import *
import json


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

    def __str__(self):
        """ introduces a character using the str method"""

        return f"Name: {self.name}\nQuirk: {self.quirk}\nStatus: {self.role}"

    @classmethod
    def population(cls):
        """ Prints the total number of people in the session """

        print(f"There are {cls._Person__population} {cls.role} in the world")

    @classmethod
    def quirks(cls):
        """ prints the remaining quirks """

        print("Quirks left: {}".format(len(quirk_list)))

    def update(self, *args, **kwargs):
        """
            Updates a player's stats
            args is strictly in order: name, role, quirk
        """

        if args is not None and len(args) != 0:
            key = ['name', 'quirk', 'role']
            for i in range(len(args)):
                try:
                    if key[i] == 'role':
                        setattr(self, key[i], role(args[i]))
                    else:
                        setattr(self, key[i], args[i])
                except IndexError:
                    pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance """

        keys = ['name', 'quirk']
        result = {}
        for instance in keys:
            result[instance] = getattr(self, instance)
        result['role'] = self.role.__str__()

        return result

    @staticmethod
    def to_json_string(list_dicts):
        """ returns the json string representation of the dictionaries """

        if list_dicts is None:
            return "[]"
        else:
            return json.dumps(list_dicts)
