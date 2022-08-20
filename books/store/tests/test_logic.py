# from django.test import TestCase
from unittest import TestCase
from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(1, 1, '+')
        self.assertEqual(2, result)


    def test_minus(self):
        result = operations(5, 1, '-')
        self.assertEqual(4, result)

    def test_multiply(self):
        result = operations(5, 5, '*')
        self.assertEqual(25, result)

    def test_devision(self):
        result = operations(25, 5, '/')
        self.assertEqual(5, result)
