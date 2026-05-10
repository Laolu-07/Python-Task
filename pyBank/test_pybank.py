import unittest

import pybank

class TestValidateEmail(unittest.TestCase):

   def test_that_validate_email_function_exists(self):
      pybank.validate_email("musa.kayode@.com")

   def test_that_valid_email_has_minimum_of_8_characters(self):
       is_valid = pybank.validate_email("musa.kayode@.com")
       self.assertTrue(is_valid)

   def test_that_valid_email_is_less_than_8_characters_return_false(self):
       is_valid = pybank.validate_email("musa")
       self.assertFalse(is_valid)

   def test_that_valid_email_contains_special_character (self):
        actual = pybank.validate_email("musa.kayode@.com")
        expected = "valid email"
        self.assertEqual(actual, expected)
