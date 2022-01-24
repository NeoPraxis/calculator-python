import io
import unittest
from unittest import mock
from unittest.mock import patch
from setuptools import setup
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    # Use this so I do not have to keep retyping calculator = Calculator(), but I have to put self. in front of any "calculator"
    def setUp(self) -> None:
        self.calculator = Calculator()

    def get_input(self, fake_input):
        with unittest.mock.patch('builtins.input', return_value=fake_input):
            self.calculator.get_user_expression()
    
    def assert_calculation(self, tokens, value):
        
        calculated_value = self.calculator.calculate_value(tokens)
        self.assertEqual(calculated_value, value)
            

            
    # Use this for verification of instance for the Class
    def test_if_calculator_can_instantiate(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_get_user_expression_stores_tokens(self):
        self.get_input('2 + 2')
        self.assertIsInstance(self.calculator.expression, str)

    def test_parse_expression_into_tokens(self):
        self.get_input('2 + 2')
        self.calculator.parse_expression_into_tokens()
        self.assertIsInstance(self.calculator.tokens, list)

    def test_validate_token_length_returns_false_if_less_than_three_tokens(self):
        self.get_input('+ 2')
        self.calculator.parse_expression_into_tokens()
        are_tokens_valid = self.calculator.validate_token_length(self.calculator.tokens)
        self.assertFalse(are_tokens_valid)

    def test_validate_token_data(self):
        self.get_input('2 + 2')
        self.calculator.parse_expression_into_tokens()
        are_tokens_valid = self.calculator.validate_token_length(self.calculator.tokens)
        self.assertTrue(are_tokens_valid)

    def test_is_number_token_returns_false_if_not_a_number(self):
        is_number = self.calculator.is_number_token('=')
        self.assertFalse(is_number)
    
    def test_if_number_token_returns_true_if_number(self):
        is_number = self.calculator.is_number_token('1')
        self.assertTrue(is_number)

    def test_is_operator_token_returns_false_if_not_a_operator(self):
        is_operator = self.calculator.is_operator_token('p')
        self.assertFalse(is_operator)

    def test_is_operator_token_returns_true_if_operator(self):
        is_operator = self.calculator.is_operator_token('*')
        self.assertTrue(is_operator)

    def test_is_valid_expression_returns_false_if_not_valid(self):
        tokens = ['awd', 'adw', 'wasd', 'dddddddd', 'baddatablabla']
        is_valid_expression = self.calculator.is_valid_expression(tokens)
        self.assertFalse(is_valid_expression)

    def test_is_valid_expression_returns_true_if_valid(self):
        tokens = ['2', '+', '2']
        is_valid_expression = self.calculator.is_valid_expression(tokens)
        self.assertTrue(is_valid_expression)

    def test_calculate_expression(self):
        self.assert_calculation(['2', '+', '2'], 4)
        self.assert_calculation(['3', '+', '3'], 6)
        self.assert_calculation(['3', '*', '3'], 9)
        self.assert_calculation(['3', '/', '3'], 1)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calculated_value(self, mock_stdout):
        self.calculator.print_calculated_value(69)
        output = mock_stdout.getvalue()
        self.assertEqual(output, '= 69\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_calculator(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value= '2 + 2'):
            self.calculator.start_calculator()
        output = mock_stdout.getvalue()
        self.assertEqual(output, '= 4.0\n')

    
if __name__ == '__main__':
    unittest.main()


# Assert is the "I expect it to: ...." method.
# Use self if we are doing anything within the class
# assertIsInstance = in this instance it should "..."
# Args or Params need to be passed in to a method to test that they will do what they are supposed to
# When passing an assert, THIS == THAT is the argument made