import unittest

import sys
sys.path.insert(0, 'interpolation')
from module import parabolic_interpolation

class TestLinearInterpolation(unittest.TestCase):

    def test_interpolation_at_node(self):
        x_values = [1, 2, 3, 4]
        y_values = [1, 0, 1, 0]

        for i in range(len(x_values)):
            result = parabolic_interpolation(x_values, y_values, x_values[i])
            self.assertEqual(result, y_values[i])

    def test_interpolation_at_arbitrary_point(self):
        x_values = [1, 2, 3, 4]
        y_values = [1, 0, 1, 0]

        result = parabolic_interpolation(x_values, y_values, 2.5)
        self.assertAlmostEqual(result, 0.5, delta=1e-6)

    def test_interpolation_with_empty_lists(self):
        result = parabolic_interpolation([], [], 2.)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()