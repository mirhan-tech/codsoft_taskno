class FormatInput:

    def __init__(self):
        self.expression = input("Enter expression in pattern 'num_1 operator num_2': ")

    def format_exp(self):
        exp = self.expression.split(" ")
        try:
            val1 = float(exp[0])
            oper = exp[1]
            val2 = float(exp[2])
            return val1, val2, oper
        except ValueError:
            print("Got anything other than numbers!")

class Calculator:

    def __init__(self, in_num1, in_num2, op_choice):
        self.num1 = in_num1
        self.num2 = in_num2
        self.choice = op_choice
        self.result = 0

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Division by Zero not possible !"

    def operation(self):
        if self.choice == '+':
            self.result = self.add()
        elif self.choice == '-':
            self.result = self.subtract()
        elif self.choice == '*' or self.choice == 'x':
            self.result = self.multiply()
        elif self.choice == '/':
            self.result = self.divide()
        else:
            self.result = "Invalid operator choice !!"
        return self.result

if __name__ == '__main__':
    while True:
        user_input = FormatInput()
        try:
            num1, num2, op = user_input.format_exp()
            print(f"First Number = {num1}\nOperator = {op}\nSecond Number = {num2}")
            calc = Calculator(num1, num2, op)
            result = calc.operation()
            print(f"{num1} {op} {num2} = {result}")
        except TypeError:
            print("Please enter numbers and try again!")
        finally:
            in_end = input("Do you want to continue calculation (yes/no): ")
            if in_end.lower() != 'yes':
                break
