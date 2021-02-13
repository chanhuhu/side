import unittest
from typing import Callable

line: Callable[[int,int], str] = lambda n, i: ((n - 1) // 2 - i) * ' ' + (2*i+1) * '*'

def diamond(n: int) -> list[str]:
    result = []
    sum=""
    for i in range(n):
        sum += line(n,i)

        result.append(sum)

    return result

class Test(unittest.TestCase):

    def test_input_n_equals_1(self):
        expect = ["*"]
        self.assertEqual(diamond(1),expect)

    def test_input_n_equals_2(self):
        expect = ["*",
                  "*"]
        self.assertEqual(diamond(2),expect)

    def test_input_n_equals_3(self):
        expect = [" * ",
                  "***",
                  " * "]
        self.assertEqual(diamond(3),expect)

if __name__ == "__main__":
    unittest.main()

