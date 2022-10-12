import unittest
import ms_math
import ms_string

class MsMathTestCase(unittest.TestCase):
    def test_sum(self):
        sum = ms_math.sum(8, 12)
        self.assertEqual(sum, 20)

    def test_multiplication(self):
        ans = ms_math.multiplication(2, 10)
        self.assertEqual(ans, 20)

    def test_division(self):
        ans = ms_math.division(10, 5)
        self.assertEqual(ans, 2)

if __name__ == '__main__':
    unittest.main()