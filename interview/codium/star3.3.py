import unittest

def star3(n: int) -> list[str]:
    result = []
    for i in range(1, n+1):
        sum = ""
        for j in range(1,n-i+1):
            sum += " "
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                sum += "*"
            else:
                sum += " "
        result.append(sum)
    return result

class Test(unittest.TestCase):

    def test_input_n_equals_1(self):
        n = 1
        self.assertEqual(star3(n),["*"])

    def test_input_n_equals_2(self):
        n = 2
        self.assertEqual(star3(n),[" *",
                                   "* *"])

    def test_input_n_equals_3(self):
        n = 3
        self.assertEqual(star3(n),['  *',
                                   ' * *',
                                   '*   *'])

    def test_input_n_equals_4(self):
        n = 4
        self.assertEqual(star3(n),['   *',
                                   '  * *',
                                   ' *   *',
                                   '*     *'])

if __name__ == "__main__":
    unittest.main()

