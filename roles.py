""" defines roles """

import random


class Citizen:
    """ defines a citizen """

    __citizen_count = 0

    def __init__(self):
        Citizen.__citizen_count += 1

    def __str__(self):
        """ Overrides the default str """

        return "Citizen"


class Student:
    """ defines a student """

    __student_count = 0

    def __init__(self):
        Student.__student_count += 1

    def __str__(self):
        """ Overrides the default str """

        return "Student"


class Pro:
    """ defines a pro """

    __pro_count = 0

    def __init__(self):
        Pro.__pro_count += 1

    def __str__(self):
        """ Overrides the default str """

        return "Pro"


class Villan:
    """ defines a villan """

    __villan_count = 0

    def __init__(self):
        Villan.__villan_count += 1

    def __str__(self):
        """ Overrides the default str """

        return "Villan"


def role(status=None):
    """ assigns a role to a person class """

    role_key_class = {
            0: Citizen,
            1: Student,
            2: Pro,
            3: Villan
    }

    if status is not None:
        name_to_key = {
                "Citizen": 0,
                "Student": 1,
                "Pro": 2,
                "Villan": 3
                }
        rl_key = name_to_key[status]
    else:
        rl_key = random.randint(0, len(role_key_class) - 1)

    rl_value = role_key_class[rl_key]
    return rl_value()
