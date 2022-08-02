import unittest
from unittest import TestCase

from apps.cat import Cat

'''
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
'''


class CatTests(TestCase):
    NAME = 'Pepelyashka'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_increment(self):
        self.cat.eat()
        self.assertEqual()

    def test_eat__expect_to_be_true(self):
        pass

    def test_eat__when_fed_is_true_expect_to_raise(self):
        pass

    def test_sleep__when_fed_is_false__expect_to_raise(self):
        pass

    def test_sleep__expect_sleepy_to_be_false(self):
        pass