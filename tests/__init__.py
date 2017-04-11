import unittest
import rasims_math
class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(rasims_math.sum_two_numbers(22, 15), 37)
if __name__ == '__main__':
    unittest.main()