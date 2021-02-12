import unittest

def diamond(n: int) -> list[str]:
    result = []
    for i in range(1, n+1):
        sum = ""
        difference = " " * (n - i)
        sum += difference
        sum += "*"
        sum += difference

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

