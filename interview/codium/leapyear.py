import unittest
import calendar

INPUT_SAMPLE = """\
1600 -> True
2000 -> True
1500 -> False
2004 -> True
2008 -> True
2010 -> False
"""


def isleap(year: int) -> bool:
    if year % 400 == 0:
        return True

    if year % 400 != 0 and year % 100 != 0 and year % 4 == 0:
        return True

    return False


class Test(unittest.TestCase):
    def test_input_sample(self):
        lines = INPUT_SAMPLE.splitlines()
        for line in lines:
            input, result = line.split(" -> ")
            input = int(input)
            result = eval(result)
            print(f"{input}: {isleap(input)} expected_result: {result}")
            self.assertEqual(isleap(input), result)


if __name__ == "__main__":
    unittest.main()
