# help me write a code for a calculator
# 1. ask the user for the operation
# 2. ask the user for the numbers
# 3. perform the operation
# 4. output the result

# Define a function to perform addition
def add(x, y):
    return x + y

# Define a function to perform subtraction
def subtract(x, y):
    return x - y

# Define a function to perform multiplication
def multiply(x, y):
    return x * y

# Define a function to perform division
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display the available operations
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get input from the user for the operation to perform
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divide(num1, num2)
else:
    print("Invalid choice")
    exit()

# Display the result
print("Result: ", result)