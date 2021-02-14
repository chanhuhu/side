from typing import Callable
from typing import Literal
from typing import TypeVar
import unittest

L = Literal['A','C']
R = Literal['B','D']

line: Callable[[int,int,L,R],str] = lambda n, i, left_letter, right_letter: (n - i) * left_letter + '+' + (n - i) * right_letter
line2: Callable[[int,int,L,R],str] = lambda n, i, left_letter, right_letter: (n - i -1) * left_letter + '+' + ((2 * i) - 1) * 'E' + '+' + (n - i -1) * right_letter

def doormat(n: int) -> list[str]:

    if n == 1:
        return ['+']
    top = [line(n,1,'A','B')]

    """
    if range(1,5-1) = [1,2,3] -> (E * ((2*1) -1) = 'E',(E * ((2*2) -1) = 'EEE'),(E * ((2*3) -1) = 'EEEEE')
    if range(1,4-1) = [1,2]   -> (E * ((2*1) -1) = 'E',(E * ((2*2) -1) = 'EEE')
    if range(1,3-1) = [1]     -> (E * ((2*1) -1) = 'E'
    """
    top_to_middle = [line2(n,i,'A','B') for i in range(1, (n//2)+1)]
    middle = ['+' + 'E' * (2 * n - 3) + '+'] 
    middle_to_bottom = list(reversed([line2(n,i,'C','D') for i in range(1, (n//2)+1)]))
    bottom = [line(n,1,'C','D')]
    result = top + middle + bottom

    if n >= 3:
        result = top + top_to_middle + middle + middle_to_bottom + bottom
        return result

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

    def test_n_equals_4(self):
        solution = ['AAA+BBB',
                    'AA+E+BB',
                    'A+EEE+B',
                    '+EEEEE+',
                    'C+EEE+D',
                    'CC+E+DD',
                    'CCC+DDD']
        self.assertEqual(doormat(4), solution)

if __name__ == "__main__":
    unittest.main()

