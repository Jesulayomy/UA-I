""" defines roles """

import random


class Citizen:
    """ defines a citizen """

    __citizen_count = 0

    def __init__(self):
        Citizen.__citizen_count += 1
        print("I am a Citizen!")

    def __str__(self):
        """ Overrides the default str """

        return "Citizen"


class Student:
    """ defines a student """

    __student_count = 0

    def __init__(self):
        Student.__student_count += 1
        print("I am a Student!")


    def __str__(self):
        """ Overrides the default str """

        return "Student"

class Pro:
    """ defines a pro """

    __pro_count = 0

    def __init__(self):
        Pro.__pro_count += 1
        print("I am a Pro!")

    def __str__(self):
        """ Overrides the default str """

        return "Pro"

class Villan:
    """ defines a villan """

    __villan_count = 0

    def __init__(self):
        Villan.__villan_count += 1
        print("I am a Villan!")

    def __str__(self):
        """ Overrides the default str """

        return "Villan"

def role():
    """ assigns a role to a person class """

    rl_dict = {
            0: Citizen,
            1: Student,
            2: Pro,
            3: Villan
    }

    rl_key = random.randint(0, len(rl_dict) - 1)
    rl_value = rl_dict[rl_key]
    return rl_value()

