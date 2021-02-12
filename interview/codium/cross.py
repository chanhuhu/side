import unittest


def cross(n: int) -> list[str]:
    result = []

    for i in range(n):
        sum = ""
        for j in range(n):
            if i == j or n - i - 1 == j:
                sum += "*"
            else:
                sum += " "
        result.append(sum)

    return result


class Test(unittest.TestCase):
    def test_input_n_equals_1(self):
        n = 1
        self.assertEqual(cross(n), ["*"])

    def test_input_n_equals_2(self):
        n = 2
        self.assertEqual(cross(n), ["**", "**"])

    def test_input_n_equals_3(self):
        n = 3
        self.assertEqual(cross(n), ["* *", " * ", "* *"])

    def test_input_n_equals_4(self):
        n = 4
        self.assertEqual(cross(n), ["*  *", " ** ", " ** ", "*  *"])

    def test_input_n_equals_5(self):
        n = 5
        self.assertEqual(cross(n), ["*   *", " * * ", "  *  ", " * * ", "*   *"])


if __name__ == "__main__":
    unittest.main()
