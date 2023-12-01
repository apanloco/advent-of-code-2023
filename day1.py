import unittest


def calibration_value(input):
    first = next(i for i, c in enumerate(input) if c.isdigit())
    last = next(i for i, c in enumerate(input[::-1]) if c.isdigit())
    return int(input[first] + input[len(input) - 1 - last])


def compute(input):
    return sum(
        calibration_value(line)
        for line in filter(None, (line.rstrip() for line in input.splitlines()))
    )


def calibration_value2(input):
    numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    result = ""
    for i in range(len(input)):
        for n, val in numbers_dict.items():
            if input[i : i + len(n)] == n:
                result += val
                break
        if len(result) == 1:
            break
    assert len(result) == 1
    for i in reversed(range(len(input))):
        for n, val in numbers_dict.items():
            if input[i : i + len(n)] == n:
                result += val
                break
        if len(result) == 2:
            break
    return int(result)


def compute2(input):
    return sum(
        calibration_value2(line)
        for line in filter(None, (line.rstrip() for line in input.splitlines()))
    )


class TestsPart1(unittest.TestCase):
    data_test = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

    def test_calibration_value(self):
        self.assertEqual(calibration_value("1abc2"), 12)
        self.assertEqual(calibration_value("pqr3stu8vwx"), 38)
        self.assertEqual(calibration_value("a1b2c3d4e5f"), 15)
        self.assertEqual(calibration_value("treb7uchet"), 77)
        pass

    def test(self):
        self.assertEqual(compute(self.data_test), 142)
        pass


class TestsPart2(unittest.TestCase):
    data_test = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

    def test_calibration_value(self):
        self.assertEqual(calibration_value2("two1nine"), 29)
        self.assertEqual(calibration_value2("eightwothree"), 83)
        self.assertEqual(calibration_value2("abcone2threexyz"), 13)
        self.assertEqual(calibration_value2("xtwone3four"), 24)

    def test(self):
        self.assertEqual(compute2(self.data_test), 281)


if __name__ == "__main__":
    data = open("day1.txt", "r").read()
    print(compute(data))
    print(compute2(data))
