from unittest import TestCase

from src.main.part1 import BasicUtilities, IntegerArrayUtilities, WuTangConcatenator


class IsBetween5And7Test(TestCase):
    def test_s(self):
        self.util(0, False)

    def test_s1(self):
        self.util(1, False)

    def test_s2(self):
        self.util(6, True)

    def test_s3(self):
        self.util(5, True)

    def test_s4(self):
        self.util(7, True)

    def util(self, value_to_evaluate, expected_outcome):
        actual_outcome = BasicUtilities.between5_7(value_to_evaluate)
        self.assertEqual(expected_outcome, actual_outcome)


class IsGreaterThan5Test(TestCase):
    def test_s(self):
        self.util(5, True)

    def test_s1(self):
        self.util(4, False)

    def test_s2(self):
        self.util(6, True)

    def test_s3(self):
        self.util(7, True)

    def util(self, value_to_evaluate, expected_outcome):
        actual_outcome = BasicUtilities.greaterthan_5(value_to_evaluate)
        self.assertEqual(expected_outcome, actual_outcome)


class IsLessThan7Test(TestCase):
    def test_s(self):
        self.util(5, True)

    def test_s1(self):
        self.util(4, True)

    def test_s2(self):
        self.util(7, True)

    def test_s3(self):
        self.util(8, False)

    def util(self, value_to_evaluate, expected_outcome):
        actual_outcome = BasicUtilities.lessthan_7(value_to_evaluate)
        self.assertEqual(expected_outcome, actual_outcome)


class StartsWithTest(TestCase):
    def test_s(self):
        self.util("The", 'T', True)

    def test_s1(self):
        self.util("The", 't', True)

    def test_s2(self):
        self.util("jump", 'z', False)

    def test_s3(self):
        self.util("tractor", 'f', False)

    def util(self, string, character, expected_outcome):
        actual_outcome = BasicUtilities.starts_with(string, character)
        self.assertEqual(expected_outcome, actual_outcome)


class GetProductOfLastTwoTest(TestCase):
    def test_s(self):
        input_array = [1, 2, 4]
        expected_sum = 2
        self.util(input_array, expected_sum)

    def test_s1(self):
        input_array = [4, 0]
        expected_sum = 0
        self.util(input_array, expected_sum)

    def test_s2(self):
        input_array = [10, 20, 4]
        expected_sum = 200
        self.util(input_array, expected_sum)

    def util(self, input_array, expected_sum):
        actual_sum = IntegerArrayUtilities.product_first_two(input_array)
        self.assertEqual(expected_sum, actual_sum)


class GetSumOfFirstTwoTest(TestCase):
    def test_s(self):
        input_array = [1, 2, 4]
        expected_sum = 3
        self.util(input_array, expected_sum)

    def test_s1(self):
        input_array = [4, 0]
        expected_sum = 4
        self.util(input_array, expected_sum)

    def test_s2(self):
        input_array = [10, 20, 4]
        expected_sum = 30
        self.util(input_array, expected_sum)

    def util(self, input_array, expected_sum):
        actual_sum = IntegerArrayUtilities.sum_first_two(input_array)
        self.assertEqual(expected_sum, actual_sum)


class HasEvenLengthTest(TestCase):
    def test_s(self):
        input_array = []
        self.util(input_array, True)

    def test_s1(self):
        input_array = [0]
        self.util(input_array, False)

    def test_s2(self):
        input_array = [0, 0]
        self.util(input_array, True)

    def test_s3(self):
        input_array = [1, 2, 3]
        self.util(input_array, False)

    def util(self, input_array, expectedOutcome):
        actual_outcome = IntegerArrayUtilities.even_length(input_array)
        self.assertEqual(actual_outcome, expectedOutcome)


class RangeTest(TestCase):

    def test_s1(self):
        start = -10
        stop = 0
        expected = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
        self.util(start, stop, expected)

    def test_s2(self):
        start = 0
        stop = 10
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.util(start, stop, expected)

    def test_s3(self):
        start = 5
        stop = 10
        expected = [5, 6, 7, 8, 9, 10]
        self.util(start, stop, expected)

    def util(self, start, stop, expected):
        actual = IntegerArrayUtilities.range(start, stop)
        self.assertEqual(expected, actual)


class WuTangConcatenatorTest(TestCase):
    def test_five(self):
        test_input = 5
        wtc = WuTangConcatenator(test_input)

        is_wu = wtc.is_wu()
        is_tang = wtc.is_tang()
        is_wu_tang = wtc.is_wu_tang()

        self.assertFalse(is_wu)
        self.assertTrue(is_tang)
        self.assertFalse(is_wu_tang)

    def test_three(self):
        test_input = 3
        wtc = WuTangConcatenator(test_input)

        is_wu = wtc.is_wu()
        is_tang = wtc.is_tang()
        is_wu_tang = wtc.is_wu_tang()

        self.assertTrue(is_wu)
        self.assertFalse(is_tang)
        self.assertFalse(is_wu_tang)

    def test_ten(self):
        test_input = 10
        wtc = WuTangConcatenator(test_input)

        is_wu = wtc.is_wu()
        is_tang = wtc.is_tang()
        is_wu_tang = wtc.is_wu_tang()

        self.assertFalse(is_wu)
        self.assertTrue(is_tang)
        self.assertFalse(is_wu_tang)

    def test_six(self):
        test_input = 6
        wtc = WuTangConcatenator(test_input)

        is_wu = wtc.is_wu()
        is_tang = wtc.is_tang()
        is_wu_tang = wtc.is_wu_tang()

        self.assertTrue(is_wu)
        self.assertFalse(is_tang)
        self.assertFalse(is_wu_tang)

    def test_fifteen(self):
        test_input = 15
        wtc = WuTangConcatenator(test_input)

        is_wu = wtc.is_wu()
        is_tang = wtc.is_tang()
        is_wu_tang = wtc.is_wu_tang()

        self.assertTrue(is_wu)
        self.assertTrue(is_tang)
        self.assertTrue(is_wu_tang)
