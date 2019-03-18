from typing import List
from unittest import TestCase

from src.main.part3 import Animal, Horse, BlueJay, RedRobin


class BlueJayTest(TestCase):
    def test_move(self):
        blue_jay = BlueJay()
        expected = "fly"
        actual = blue_jay.move
        self.assertEqual(expected, actual)

    def test_color(self):
        blue_jay = BlueJay()
        expected = "blue"
        actual = blue_jay.color
        self.assertEqual(expected, actual)


class HorseTest(TestCase):
    def test_move(self):
        horse = Horse()
        expected = "gallop"
        actual = horse.move
        self.assertEqual(expected, actual)

    def test_color(self):
        horse = Horse()
        expected = "brown"
        actual = horse.color
        self.assertEqual(expected, actual)


class RedRobinTest(TestCase):
    def test_move(self):
        red_robin = RedRobin()
        expected = "fly"
        actual = red_robin.move
        self.assertEqual(expected, actual)

    def test_migration_month(self):
        red_robin = RedRobin()
        expected = "August"
        red_robin.migration_month = expected
        actual = red_robin.migration_month
        self.assertEqual(expected, actual)

    def test_color(self):
        red_robin = RedRobin()
        expected = "red"
        actual = red_robin.color
        self.assertEqual(expected, actual)


class SpeedComparatorTest(TestCase):
    def test_array_sort(self):
        horse: Animal = Horse()
        blue_jay: Animal = BlueJay()
        red_robin: Animal = RedRobin()

        animals: List[Animal] = [red_robin, horse, blue_jay]
        animals.sort(reverse= True, key=lambda animal: animal.speed)

        self.assertEqual(horse, animals[0])
        self.assertEqual(blue_jay, animals[1])
        self.assertEqual(red_robin, animals[2])
