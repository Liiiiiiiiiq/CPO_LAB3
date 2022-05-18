import unittest
from math import sin
from hypothesis import given

import hypothesis.strategies as st

from expression_tree import *


class TestExpressTree(unittest.TestCase):

    def test_example(self):
        sting = 'a + 2 - sin(-0.3)*(b - c)'
        fun = ExpressTree(sting, sin=lambda a: sin(a))
        # fun.visualization()
        t0 = 4 + 2 - sin(-0.3) * (2 - 66)
        self.assertEqual(t0, fun(a=4, b=2, c=66))
