import unittest
from typing import Callable

line: Callable[[int,int], str] = lambda n, i: ((n  // 2) - i) * ' '\
                                                    + (2*i+1) * '*'
even: Callable[[int], bool] = lambda n: n % 2 == 0

odd: Callable[[int], bool] = lambda n: not even(n)


def diamond(n: int) -> list[str]:
    upper = [line(n,i) for i in range(n//2)]
    lower = list(reversed(upper))
    result = upper + lower

    # static analysis a.k.a. fix bug run time
    if n == 1:
        return ['*']
    elif n == 2:
        return ['*','*']
    elif odd(n):
        return upper + ['*'* n] + lower


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
    for i in diamond(9):
        print(i)
    print('*9'*10)
        
    for i in diamond(5):
        print(i)
    print('*5'*10)

    for i in diamond(4):
        print(i)
    print('*4'*10)

    for i in diamond(3):
        print(i)
    print('*3'*10)

    for i in diamond(2):
        print(i)
    print('*2'*10)

    for i in diamond(1):
        print(i)
    print('*1'*10)
