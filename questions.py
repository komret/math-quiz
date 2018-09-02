class Question:
    answer = None
    text = None


class Add(Question):
    def __init__(self, num1, num2):
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2

    def __str__(self):
        return "Add"


class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = '{} x {}'.format(num1, num2)
        self.answer = num1 * num2

    def __str__(self):
        return "Multiply"


class Subtract(Question):
    def __init__(self, num1, num2):
        self.text = '{} - {}'.format(num1, num2)
        self.answer = num1 - num2

    def __str__(self):
        return "Subtract"


class Divide(Question):
    def __init__(self, num1, num2):
        self.text = '{} : {}'.format(num1, num2)
        self.answer = int(num1 / num2)

    def __str__(self):
        return "Divide"
