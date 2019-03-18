from typing import List


class BasicUtilities:
    @staticmethod
    def greaterthan_5(value_to_evaluate: int) -> bool:
        return value_to_evaluate >= 5

    @staticmethod
    def lessthan_7(value_to_evaluate: int) -> bool:
        return value_to_evaluate <= 7

    @staticmethod
    def between5_7(value_to_evaluate: int) -> bool:
        return 7 >= value_to_evaluate >= 5

    @staticmethod
    def starts_with(string: str, character: str) -> bool:
        return string[0].upper() == character.upper()


class IntegerArrayUtilities:
    @staticmethod
    def even_length(input_array: List[int]) -> bool:
        return len(input_array) % 2 == 0

    @staticmethod
    def range(start: int, stop: int) -> List[int]:
        return list(range(start, stop + 1))

    @staticmethod
    def sum_first_two(input_array: List[int]) -> int:
        return sum(input_array[0:2])

    @staticmethod
    def product_first_two(input_array: List[int]) -> int:
        return input_array[0] * input_array[1]


class WuTangConcatenator:
    def __init__(self, input_int):
        self.input_int = input_int

    def is_wu(self):
        return self.input_int % 3 == 0

    def is_tang(self):
        return self.input_int % 5 == 0

    def is_wu_tang(self):
        return self.is_wu() and self.is_tang()
