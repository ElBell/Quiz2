class TestUtils:
    @staticmethod
    def assert_array_equals(self, expected, actual):
        actual.sort()
        expected.sort()
        self.assertEqual(expected, actual)
