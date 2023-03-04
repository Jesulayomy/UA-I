#!/usr/bin/env python3
""" Tests for the quirks module containing the quirks list """

import sys
import unittest
from quirks import quirk_list


class TestQuirkObjects(unittest.TestCase):
    """ Tests the quirk_list """

    def test_type(self):
        """ checks the type """

        self.assertEqual(list, type(quirk_list))

    def test_element(self):
        """ chechs the type of the elements in quirk list """

        for element in quirk_list:
            if element is not None:
                self.assertEqual(str, type(element))
