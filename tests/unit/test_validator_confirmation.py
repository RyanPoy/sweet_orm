#coding: utf8
from sweet_orm.utils.validation import ConfirmationValidator
from __init__ import TestCase


class TestValidatorConfirmation(TestCase):

    def test_confirmation(self):
        self.assertTrue(ConfirmationValidator().validate(10, 10))  

    def test_disconfirmation(self):
        self.assertFalse(ConfirmationValidator().validate(10, 100))


if __name__ == '__main__':
    import unittest
    unittest.main()
