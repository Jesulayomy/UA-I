#!/usr/bin/env python3
""" Tests for the person module """

import sys
import unittest
from person import Person
from quirks import quirk_list
from roles import role


class TestQuirkObjects(unittest.TestCase):
    """ Tests the quirk_list """

    def setUp(self):
        """ initt """

        Person._Person__population = 0

    def test_1_type(self):
        """ checks the type """

        u0 = Person("User0")
        self.assertEqual(Person, type(u0))
        self.assertEqual(Person._Person__population, 1)

    def test_2_element(self):
        """ chechs the type of the elements in quirk list """

        for i in range(1, 10):
            globals()['u%s' % i] = Person("User{0}".format(i))

        self.assertEqual(Person._Person__population, 9)

    def test_3_dicts(self):
        """ chechs the type of the elements in quirk list """

        for i in range(1, 10):
            globals()['u%s' % i] = Person("User{0}".format(i))

        d1 = u1.to_dictionary()
        d2 = u2.to_dictionary()
        d3 = u3.to_dictionary()
        d4 = u4.to_dictionary()

        print(d1)
        print(d2)
        print(d3)
        print(d4)
