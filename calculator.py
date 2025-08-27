from operations import add, subtract, multiply, divide

def get_number(prompt):
    """Validate input to accept only numbers."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

def calculator_menu():
    while True:
        print("\n=== Calculator Menu ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("👋 Exiting Calculator. Bye!")
            break

        if choice in ["1", "2", "3", "4"]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                print(f"✅ Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"✅ Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"✅ Result: {multiply(num1, num2)}")
            elif choice == "4":
                try:
                    print(f"✅ Result: {divide(num1, num2)}")
                except ZeroDivisionError:
                    print("⚠️ Cannot divide by zero!")
        else:
            print("⚠️ Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    calculator_menu()

