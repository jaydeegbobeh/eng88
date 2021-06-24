# Functional Calculator task

Create tests for functions:
1. cm to inch converter
2. remainder of val1 / val2
3. calculate area of a triangle given the base and height
4. calculate the percentage of val1 out of val2

- create class FunctCalc
```python
class FunctCalc:

    def cm_to_to_inch(self, cm_val):
        return cm_val * 2.54

    def remainder(self, val1, val2):
        return val1 % val2

    def triangle_area(self, b, h):
        return 0.5 * (b * h)

    def percentage(self, val1, val2):
        return 100 * (val1 / val2)
```
- import pytest and unittest
- import the class FunctCalc to class FunctTest
- create object funct for class FunctCalc
- define some test checks e.g for the percentage function we want to check that 4 out of 10 returns 40%

```python
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
```

