import unittest

factor = lambda n: (i for i in range(1,n+1)if n % i == 0)

is_prime = lambda n: list(factor(n)) == [1,n]

primes = lambda n : (i for i in range(2,n+1) if is_prime(i))

INPUT_SAMPLE = """\
20 -> 2 3 5 7 11 13 17 19
"""
class Test(unittest.TestCase):

    def test_input_sample(self):
        n, result = INPUT_SAMPLE.split(" -> ")
        n = int(n)
        result = list(map(int, result.split()))
        self.assertEqual(list(primes(n)),result)

if __name__ == "__main__":
    unittest.main()


