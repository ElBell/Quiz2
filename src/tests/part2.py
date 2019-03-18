from unittest import TestCase

from src.main.part2 import Router, ListUtility, ArrayUtility


class CountOccurrencesTest(TestCase):

    def test_count_occurrence_whenValueDoesNotExist(self):
        value_to_evaluate = 7
        expected = 0
        array1 = [1, 6]
        array2 = [9, 8, 11]
        actual = ArrayUtility.count_occurrence(array1, array2, value_to_evaluate)
        self.assertEqual(expected, actual)

    def count_occurrence_whenValueExistInFirstArray(self):
        value_to_evaluate = 7
        expected = 1
        array1 = [1, 6, value_to_evaluate]
        array2 = [3]
        actual = ArrayUtility.count_occurrence(array1, array2, value_to_evaluate)
        self.assertEqual(expected, actual)

    def count_occurrence_whenValueExistInSecondArray(self):
        value_to_evaluate = 9
        expected = 2
        array1 = [1, 6]
        array2 = [value_to_evaluate, value_to_evaluate, 3]
        actual = ArrayUtility.count_occurrence(array1, array2, value_to_evaluate)
        self.assertEqual(expected, actual)

    def count_occurrence_whenValueAppearsInBoth(self):
        value_to_evaluate = 7
        expected = 7
        array1 = [value_to_evaluate, 1, value_to_evaluate, 8, 84, 5, value_to_evaluate, 9, 8, value_to_evaluate]
        array2 = [1, value_to_evaluate, value_to_evaluate, 8, 5, value_to_evaluate, 91]
        actual = ArrayUtility.count_occurrence(array1, array2, value_to_evaluate)
        self.assertEqual(expected, actual)


class MergeTest(TestCase):

    def test1(self):
        array1 = [9]
        array2 = [6]
        expected = [9, 6]
        self.util(array1, array2, expected)

    def test2(self):
        array1 = [5, 1, 8]
        array2 = [4, 2]
        expected = [5, 1, 8, 4, 2]
        self.util(array1, array2, expected)

    def test3(self):
        array1 = [5, 1, 8, 9, 10]
        array2 = [4, 2, 11]
        expected = [5, 1, 8, 9, 10, 4, 2, 11]
        self.util(array1, array2, expected)

    def test4(self):
        array1 = [1993, 1994, 1995]
        array2 = [2003, 2004, 2005]
        expected = [1993, 1994, 1995, 2003, 2004, 2005]
        self.util(array1, array2, expected)

    def util(self, array1, array2, expected):
        actual = ArrayUtility.merge(array1, array2)
        self.assertEqual(expected, actual)


class MostCommonTest(TestCase):

    def testMostCommon_withOnlyOneElement(self):
        array = [5]
        expected = 5
        actual = ArrayUtility.most_common(array)
        self.assertEqual(expected, actual)

    def testMostCommon_withMultipleElements(self):
        common_value = 8
        array = [common_value, 5, 1, 1, common_value, 5, 5, common_value, common_value]
        actual = ArrayUtility.most_common(array)
        self.assertEqual(common_value, actual)


class RotateTest(TestCase):
    def test_rotate_left_for_one(self):
        array = [5, 1, 8, 4, 2]
        expected = [1, 8, 4, 2, 5]
        actual = ArrayUtility.rotate(array, 1)
        self.assertEqual(expected, actual)

    def test_rotate_left_for_more_than_one(self):
        array = [5, 1, 8, 4, 2]
        expected = [4, 2, 5, 1, 8]
        actual = ArrayUtility.rotate(array, 3)
        self.assertEqual(expected, actual)


class AddTest(TestCase):
    def test1(self):
        self.util(1)

    def test2(self):
        self.util(2)

    def test3(self):
        self.util(3)

    def test4(self):
        self.util(None)

    def util(self, value_to_add):
        utility = ListUtility()
        self.assertFalse(utility.contains(value_to_add))
        utility.add(value_to_add)
        self.assertTrue(utility.contains(value_to_add))


class GetUniqueTest(TestCase):

    def test1(self):
        values_to_add = [1, 1, 2, 3]
        unique_values = [1, 2, 3]
        self.util(values_to_add, unique_values)

    def test2(self):
        values_to_add = [1, 2, 3]
        unique_values = [1, 2, 3]
        self.util(values_to_add, unique_values)

    def test3(self):
        values_to_add = [1, 1, 2, 3, 4, 4, 6]
        unique_values = [1, 2, 3, 4, 6]
        self.util(values_to_add, unique_values)

    def util(self, values_to_add, unique_values):
        utility = ListUtility()
        expected_list = unique_values
        for value_to_add in values_to_add:
            utility.add(value_to_add)
        actual_list = utility.get_unique()
        self.assertEqual(expected_list, actual_list)


class JoinTest(TestCase):
    def testJoin_withOneElement(self):
        utility = ListUtility()
        utility.add(812)
        expected = "812"
        actual = utility.join()
        self.assertEqual(expected, actual)

    def testJoin_withMultipleElement(self):
        utility = ListUtility()
        utility.add(8)
        utility.add(7)
        utility.add(9)
        utility.add(71)
        expected = "8, 7, 9, 71"
        actual = utility.join()
        self.assertEqual(expected, actual)


class ListMostCommonTest(TestCase):

    def test1(self):
        most_common_value = 8193
        values_to_add = [most_common_value, most_common_value, most_common_value, 10]
        self.util(values_to_add, most_common_value)

    def test2(self):
        most_common_value = 6783
        values_to_add = [most_common_value, most_common_value, most_common_value, 10]
        self.util(values_to_add, most_common_value)

    def test3(self):
        most_common_value = None
        values_to_add = [most_common_value, most_common_value, most_common_value, 10]
        self.util(values_to_add, most_common_value)

    def test4(self):
        most_common_value = 999
        values_to_add = most_common_value, most_common_value, most_common_value, 10
        self.util(values_to_add, most_common_value)

    def util(self, values_to_add, most_common_value):
        utility = ListUtility()
        for value_to_add in values_to_add:
            utility.add(value_to_add)
        actual = utility.most_common()
        self.assertEqual(most_common_value, actual)


class SizeTest(TestCase):
    def test1(self):
        self.util(1)

    def test2(self):
        self.util(1, 10, 123213)

    def test3(self):
        self.util(1, 912, 1381, 12312, 13, 75657)

    def util(self, *values_to_add):
        utility = ListUtility()
        expected_size = len(values_to_add)
        for value_to_add in values_to_add:
            utility.add(value_to_add)
        actual_size = utility.size()
        self.assertEqual(expected_size, actual_size)


class RouterAddTest(TestCase):
    def test1(self):
        expected_path = "/users"
        controller = "UserController"
        self.util(expected_path, controller)

    def test2(self):
        expected_path = "/players"
        controller = "PlayerController"
        self.util(expected_path, controller)

    def test3(self):
        expected_path = "/Students"
        controller = "StudentsController"
        self.util(expected_path, controller)

    def test4(self):
        expected_path = "/myPath"
        controller = "MyController"
        self.util(expected_path, controller)

    def util(self, expected_path, controller):
        router = Router()
        router.add(expected_path, controller)
        actual_controller = router.get_controller(expected_path)
        self.assertEqual(controller, actual_controller)


class RemovePathTest(TestCase):
    def test1(self):
        self.util("/users", "UserController")

    def test2(self):
        self.util("/employees", "EmployeeController")

    def test3(self):
        self.util("/students", "StudentController")

    def util(self, path, controller):
        router = Router()
        router.add(path, controller)
        self.assertIsNotNone(router.get_controller(path))
        router.remove(path)
        self.assertIsNone(router.get_controller(path))


class RouterSizeTest(TestCase):
    def test1(self):
        self.util(
            Pair("/users", "UserController"),
            Pair("/students", "StudentController"),
            Pair("/instructors", "InstructorController"))

    def test2(self):
        self.util(
            Pair("/employees", "EmployeeController"),
            Pair("/muffins", "MuffinController"),
            Pair("/cupcakes", "CupcakeController"),
            Pair("/tests", "TestController"))

    def test3(self):
        self.util(
            Pair("/cupcakes", "CupcakeController"),
            Pair("/tests", "TestController"))

    def util(self, *entries):
        router = Router()
        expected_size = len(entries)
        for entry in entries:
            path = entry.key
            controller = entry.value
            router.add(path, controller)
        actual_size = router.size()
        self.assertEqual(expected_size, actual_size)


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ToStringTest(TestCase):
    def test1(self):
        router = Router()
        router.add("/users", "UserController")
        router.add("/students", "StudentController")
        router.add("/instructor", "InstructorController")
        expected = "/instructor -> InstructorController\n/students -> StudentController\n/users -> UserController\n"
        actual = router.to_string()
        self.assertEqual(expected, actual)


class UpdateControllerTest(TestCase):
    def test1(self):
        self.util("/users", "StudentController", "UserController")

    def test2(self):
        self.util("/employees", "UserController", "EmployeeController")

    def test3(self):
        self.util("/students", "EmployeeController", "StudentController")

    def util(self, path, original_controller, updated_controller):
        router = Router()
        router.add(path, original_controller)
        router.update(path, updated_controller)
        actual_controller = router.get_controller(path)
        self.assertEqual(updated_controller, actual_controller)
