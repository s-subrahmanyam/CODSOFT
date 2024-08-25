class Calculator:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calculate(self):
        match self.operator:
            case '+':
                return self.num1 + self.num2
            case '-':
                return self.num1 - self.num2
            case '*':
                return self.num1 * self.num2
            case '/':
                try:
                    return self.num1 / self.num2
                except ZeroDivisionError:
                    return "Error: Division by zero"
            case _:
                return "Error: Invalid operator"

if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operation (+, -, *, /): ")

            calc = Calculator(num1, num2, operator)
            result = calc.calculate()
            print(f"The result of {num1} {operator} {num2} is: {result}")
        except ValueError:
            print("Error: Invalid input, please enter numeric values.")

        again = input("Do you want to perform another calculation? (Y/N): ").lower()
        if again != 'y':
            break
