import unittest
from unittest import mock
from unittest.mock import patch
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # Use this for verification of instance for the Class
    def test_if_calculator_can_instantiate(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)
    
    # Use this for STR verification of input and for MOCK input
    def test_get_user_expression_return_string(self):
        calculator = Calculator()
        with unittest.mock.patch('builtins.input', return_value='2 + 2'):
            test_get_user_expression = calculator.get_user_expression()
            self.assertIsInstance(test_get_user_expression, str)
        

    def test_get_user_expression_stores_tokens(self):
        calculator = Calculator()
        with unittest.mock.patch('builtins.input', return_value='2 + 2'):
            test_get_user_expression_stores_tokens = calculator.get_user_expression()
            self.assertIsInstance(calculator.tokens, list)

    
if __name__ == '__main__':
    unittest.main()


# Assert is the "I expect it to: ...." method.
# Use self if we are doing anything within the class
# assertIsInstance = in this instance it should "..."
# Args or Params need to be passed in to a method to test that they will do what they are supposed to
# When passing an assert, THIS == THAT is the argument made