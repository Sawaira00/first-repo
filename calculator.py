# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
aaaaaaaaaaaaaaaaaaaa
def divide(x, y):
    return x / y  # No error handling for division by zero

def main():
    print("Welcome to the calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            break  # Missing proper exit message
        
        num1 = input("Enter first number: ")  # Input is not validated
        num2 = input("Enter second number: ")  # Input is not validated
        
        # Trying to convert input directly without validation
        num1 = float(num1)  
        num2 = float(num2)

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")  # No check for division by zero
        else:
            print("Invalid choice. Please choose a valid operation.")  # Poor error message

if __name__ == "__main__":
    main()
