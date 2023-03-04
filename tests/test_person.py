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
