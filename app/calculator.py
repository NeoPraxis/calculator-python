class Calculator:
    
    def get_user_expression(self):
        expression = input('Welcome to the calculator!\n\n')
        self.tokens = expression.split(' ')
        return 'string'
        