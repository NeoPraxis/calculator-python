
class Calculator:
    operators = ['*', '/', '+', '-', '%']

    def get_user_expression(self):
        self.expression = input('Welcome to the calculator!\n\n')

    def parse_expression_into_tokens(self):
        self.tokens = self.expression.split(' ')

    def validate_token_length(self, tokens):
        has_at_least_three_tokens = len(tokens) == 3
        return has_at_least_three_tokens
    
    def is_number_token(self, token):
        is_number = token.isnumeric()
        return is_number

    def is_operator_token(self, token):
        is_operator = token in self.operators
        return is_operator

    def is_valid_expression(self, tokens):
        is_first_token_numeric = self.is_number_token(tokens[0])
        is_second_token_an_operator = self.is_operator_token(tokens[1])
        is_third_token_numeric = self.is_number_token(tokens[2])
        return is_first_token_numeric and is_second_token_an_operator and is_third_token_numeric

    def calculate_value(self, tokens):
        number1 = float(tokens[0])
        number2 = float(tokens[2])
        operator = tokens[1]
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        value = operations[operator](number1, number2)
        return value

    def print_calculated_value(self, calculated_value):
        print(f'= {calculated_value}')

    def start_calculator(self):
        self.get_user_expression()
        self.parse_expression_into_tokens()
        is_correct_length = self.validate_token_length(self.tokens)
        is_valid = is_correct_length and self.is_valid_expression(self.tokens)
        if is_valid:
            calculated_value = self.calculate_value(self.tokens)
            self.print_calculated_value(calculated_value)
        

if __name__ == '__main__':
    calculator = Calculator()
    calculator.start_calculator()
