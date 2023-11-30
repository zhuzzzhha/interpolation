import unittest

import sys
sys.path.insert(0, 'interpolation')
from module import global_interpolation

class TestGlobalInterpolation(unittest.TestCase):

    def test_interpolation_at_node(self):
        x_values = [3, 4, 5, 6]
        y_values = [1, 0, 4, 2]

        for i in range(len(x_values)):
            result = global_interpolation(x_values, y_values, x_values[i])
            self.assertEqual(result, y_values[i])

    def test_interpolation_at_arbitrary_point(self):
        x_values = [3, 4, 5, 6]
        y_values = [1, 0, 4, 2]

        result = global_interpolation(x_values, y_values, 4.5)
        self.assertAlmostEqual(result, 2.0625, delta=1e-6)

    def test_interpolation_with_empty_lists(self):
        result = global_interpolation([], [], 4.5)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
