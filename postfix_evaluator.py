from stack import Stack

class PostfixEvaluator:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        stack = Stack()
        tokens = self.expression.split()

        for token in tokens:
            if token.isdigit():
                stack.push(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    stack.push(operand1 + operand2)
                elif token == '-':
                    stack.push(operand1 - operand2)
                elif token == '*':
                    stack.push(operand1 * operand2)
                elif token == '/':
                    stack.push(operand1 / operand2)

        return stack.pop()
