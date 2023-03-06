""" A class that defines a person as an object """

import csv
import json
import random
from roles import *
from quirks import *


class Person:
    """ defines a base class for people """

    __population = 0
    idx = 0

    def __init__(self, name):
        """ Initialization """

        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        self.name = name
        self.role = role()
        Person.__population += 1

        factor = random.randint(0, len(quirk_list))
        self.quirk = quirk_list.pop(factor)

    def __str__(self):
        """ introduces a character using the str method"""

        return f"Name: {self.name}\nQuirk: {self.quirk}\nStatus: {self.role}\n"

    @classmethod
    def population(cls, self):
        """ Prints the total number of people in the session """

        print(f"There are {cls._Person__population} {self.role} in the world")

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
                if key == 'role':
                    setattr(self, key, role(value))
                else:
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
        """
            Effectively returns the json string representation of the
            dictionary of an instance's with def attributes
        """

        if list_dicts is None:
            return "[]"
        else:
            return json.dumps(list_dicts)

    @staticmethod
    def from_json_string(json_str):
        """
            Loads a class from a json string representation
            It returns a list btw
        """

        return json.loads(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
            creates an instance using the dictionary
            always add the ** in the arg, ex: Person.create(**dict1)
        """

        new = cls("default")
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file(cls, list_person, filename=None):
        """ saves a list of people to a file """

        if filename is None:
            filename = "{}.json".format(cls.__name__)
        list_dict = []
        for obj in list_person:
            list_dict.append(obj.to_dictionary())
        json_str = cls.to_json_string(list_dict)
        with open(filename, "a") as f:
            f.write(json_str)

    @classmethod
    def load_from_file(cls, from_file=None):
        """ loads a list of people from a json file """

        if from_file is None:
            filename = f"{cls.__name__}.json"
        else:
            if type(from_file) is not str:
                raise TypeError("The filename should be a string")
            filename = from_file

        i = cls.idx
        list_people = []
        with open(filename, 'r') as fl:
            for line in fl:
                list_dict = cls.from_json_string(line)
                for j in range(len(list_dict)):
                    d = list_dict[j]
                    globals()['bot%s' % i] = cls.create(**d)
                    list_people += [globals()['bot%s' % i]]
                    i += 1

        cls.idx = i + 1

        return list_people

    @classmethod
    def save_to_csv(cls, list_people, filename=None):
        """ saves to csv """

        if filename is None:
            filename = f"{cls.__name__}.csv"

        list_keys = ['name', 'quirk', 'role']
        list_values = ['default', 'None', 'Student']
        people = []
        for obj in list_people:
            for idx in range(len(list_keys)):
                list_values[idx] = obj.to_dictionary()[list_keys[idx]]
            people.append(list_values[:])

        with open(filename, 'a') as fl:
            sheet = csv.writer(fl)
            sheet.writerows(people)

    @classmethod
    def load_from_csv(cls, filename=None):
        """ loads from csv and returns a list """

        if filename is None:
            filename = f"{cls.__name__}.csv"

        list_keys = ['name', 'quirk', 'role']

        list_people = []
        dictionary = {}
        list_dict = []
        with open(filename, 'r') as fl:
            sheet = csv.reader(fl)
            for list_row in sheet:
                for idx in range(len(list_keys)):
                    dictionary[list_keys[idx]] = list_row[idx]
                list_dict.append(dictionary)
                dictionary = {}
            for i in range(len(list_dict)):
                list_people.append(cls.create(**list_dict[i]))

        return list_people
