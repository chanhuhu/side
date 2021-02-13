import unittest

def doormat(n: int) -> list[str]:
    return ['+']


class Test(unittest.TestCase):

    def test_n_equals_1(self):
        solution = ['+']
        self.assertEqual(doormat(1), solution)


