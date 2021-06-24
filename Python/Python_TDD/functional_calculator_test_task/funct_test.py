import pytest
import unittest

from funct_calc import FunctCalc


class FunctTest(unittest.TestCase):

    funct = FunctCalc()

    def test_cm_to_inch(self):
        self.assertEqual(self.funct.cm_to_to_inch(4), 10.16)

    def test_remainder(self):
        self.assertEqual(self.funct.remainder(4, 3), 1)

    def test_triangle_area(self):
        self.assert_(self.funct.triangle_area(8, 9), 36)

    def test_percentage(self):
        self.assertEqual(self.funct.percentage(4, 10), 40)
