class Calculator:
    
    def get_user_expression(self):
        self.expression = input('Welcome to the calculator!\n\n')

    def parse_expression_into_tokens(self):
        self.tokens = self.expression.split(' ')

    def validate_token_data(self):
        has_at_least_three_tokens = len(self.tokens) >= 3
        return has_at_least_three_tokens
        