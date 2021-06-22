# Test Driven Development
## Pytest and Unittest
### use pip install to install packages

**TDD**
- starts with RED - everything failing before writing functional code
- GREEN - write the code to pass
- BLUE refactoring - then start again

- `unittest` and `pytest`

1. file to write our tests - for basic calc class
2. then we will create a file to add functionality to pass the tests, basic calculator

Writing tests:
```
import pytest
import unittest

from simple_calc import SimpleCalc
# inheriting from unittest


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self): # naming convention is essential as 'test' the word that we need to use when naming tests so python interpreter recognises it to run
        self.assertEqual(self.calc.add(2, 4), 6) # if 2 + 4 is 6 the test will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2) # if 4 - 2 is 2 the test will pass

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4) # if 2 * 2 is 4 the test will pass

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2) # if 6 / 3 is 2 the test will pass
```

- Command to run the tests `python -m unittest discover -v`

```
class SimpleCalc:


    def add(self, int1, int2):
        return int1 + int2

    def subtract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int2
```
`python -m unittest`