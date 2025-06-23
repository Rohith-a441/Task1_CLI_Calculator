# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("📟 Welcome to CLI Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("👋 Exiting calculator. Thank you!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operator = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operator = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operator = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operator = '/'

            print(f"\n✅ Result: {num1} {operator} {num2} = {result}")
        else:
            print("⚠ Invalid choice. Please choose from 1 to 5.")

if _name_ == "_main_":
    calculator()
