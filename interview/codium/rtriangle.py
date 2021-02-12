import unittest


def triangle(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        sum = ""
        space = n - i
        sum = sum.rjust(space)

        for _ in range(i):
            sum += "*"

        result.append(sum)

    return result


class Test(unittest.TestCase):
    def test_input_n_equals_3(self):
        self.assertEqual(triangle(3), ["  *", " **", "***"])

    def test_input_n_equals_4(self):
        self.assertEqual(triangle(4), ["   *", "  **", " ***", "****"])

    def test_input_n_equals_6(self):
        self.assertEqual(
            triangle(6), ["     *", "    **", "   ***", "  ****", " *****", "******"]
        )


if __name__ == "__main__":
    unittest.main()
