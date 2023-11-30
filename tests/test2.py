import unittest

import sys
sys.path.insert(0, 'interpolation')
from module import linear_inperpolation

class TestLinearInterpolation(unittest.TestCase):

    def test_interpolation_at_node(self):
        x_values = [1, 3, 4, 5, 7]
        y_values = [5, 2, 7, 4, 1]

        for i in range(len(x_values)):
            result = linear_inperpolation(x_values, y_values, x_values[i])
            self.assertEqual(result, y_values[i])

    def test_interpolation_at_arbitrary_point(self):
        x_values = [1, 3, 4, 5, 7]
        y_values = [5, 2, 7, 4, 1]

        result = linear_inperpolation(x_values, y_values, 2)
        self.assertAlmostEqual(result, 3.5, delta=1e-6)

    def test_interpolation_with_empty_lists(self):
        result = linear_inperpolation([], [], 2)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()