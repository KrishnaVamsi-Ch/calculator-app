def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("🧮 Welcome to the Python Calculator!")
    print("Select operation: +  -  *  /")

    while True:
        choice = input("Enter operator (+, -, *, /) or 'q' to quit: ")

        if choice == 'q':
            print("Goodbye!")
            break

        if choice in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)

            print(f"Result: {result}\n")
        else:
            print("Invalid operator.")

if __name__ == "__main__":
    calculator()
