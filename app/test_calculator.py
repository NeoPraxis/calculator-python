import unittest
from unittest import mock
from unittest.mock import patch
from setuptools import setup
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # Use this so I do not have to keep retyping calculator = Calculator(), but I have to put self. in front of any "calculator"
    def setUp(self) -> None:
        self.calculator = Calculator()

    # Use this for verification of instance for the Class
    def test_if_calculator_can_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_get_user_expression_stores_tokens(self): 
        with unittest.mock.patch('builtins.input', return_value='2 + 2'):
            self.calculator.get_user_expression()
            self.assertIsInstance(self.calculator.expression, str)

    def test_parse_expression_into_tokens(self):
        with unittest.mock.patch('builtins.input', return_value='2 + 2'):
            self.calculator.get_user_expression()
            self.calculator.parse_expression_into_tokens()
            self.assertIsInstance(self.calculator.tokens, list)

    def test_validate_token_data_returns_false_if_less_than_three_tokens(self):
        with unittest.mock.patch('builtins.input', return_value='+ 2'):
            self.calculator.get_user_expression()
            self.calculator.parse_expression_into_tokens()
        are_tokens_valid = self.calculator.validate_token_data()
        self.assertFalse(are_tokens_valid)

    def test_validate_token_data(self):
        with unittest.mock.patch('builtins.input', return_value='2 + 2'):
            self.calculator.get_user_expression()
            self.calculator.parse_expression_into_tokens()
        are_tokens_valid = self.calculator.validate_token_data()
        self.assertTrue(are_tokens_valid)

    def test_determine_expression_operator(self):
        pass

    def test_calculate_expression(self):
        pass

    def test_print_calculated_value(self):
        pass

    
if __name__ == '__main__':
    unittest.main()


# Assert is the "I expect it to: ...." method.
# Use self if we are doing anything within the class
# assertIsInstance = in this instance it should "..."
# Args or Params need to be passed in to a method to test that they will do what they are supposed to
# When passing an assert, THIS == THAT is the argument made