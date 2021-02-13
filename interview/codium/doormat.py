from typing import Callable, Literal
from typing import TypeVar
import unittest

L = Literal['A','C']
R = Literal['B','D']

line: Callable[[int,int,L,R],str] = lambda n, i, left, right: (n - i) * left + '+' + (n -i) * right

def doormat(n: int) -> list[str]:
    if n == 1:
        return ['+']

    top = [line(n,i,'A','B') for i in range(1,(n//2)+1)]
    middle = ['+' + 'E' '+']
    bottom = [line(n,i,'C','D') for i in range(1,(n//2)+1)]
    result = top + middle + bottom
    
    return result


class Test(unittest.TestCase):

    def test_n_equals_1(self):
        solution = ['+']
        self.assertEqual(doormat(1), solution)

    def test_n_equals_2(self):
        solution = ['A+B',
                    '+E+',
                    'C+D']
        self.assertEqual(doormat(2), solution)

    def test_n_equals_3(self):
        solution = ['AA+BB',
                    'A+E+B',
                    '+EEE+',
                    'C+E+D',
                    'CC+DD']
        self.assertEqual(doormat(3), solution)
if __name__ == "__main__":
    unittest.main()


