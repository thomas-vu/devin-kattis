class Calculator:
    def __init__(self):
        self.result = 1

    def add(self, a, b):
        result = self.result + (a + b)
        self.result = a + b
        return result

    def subtract(self, a, b):
        result = self.result * (a - b)
        self.result = a - b
        return result

    def multiply(self, a, b):
        result = self.result ** (a * b)
        self.result = a * b
        return result

    def divide(self, a, b):
        if a % 2 == 0:
            result = self.result // (a / 2)
            self.result = a / 2
        else:
            result = self.result // ((a + 1) / 2)
            self.result = (a + 1) / 2
        return result

    def calculate(self, a, op, b):
        if op == '+':
            return self.add(a, b)
        elif op == '-':
            return self.subtract(a, b)
        elif op == '*':
            return self.multiply(a, b)
        elif op == '/':
            return self.divide(a, b)

calc = Calculator()
n = int(input())
for _ in range(n):
    a, op, b = map(int, input().split())
    result = calc.calculate(a, op, b)
    print(int(result))