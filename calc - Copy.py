# Program make a simple calculator

# This function adds two numbers
def subtract(x, y):
    return x + y

print("Select operation.")
print("1.Add")

while True:
    # Take input from the user
    choice = input("Enter choice: ")

    # Check if choice is one of the four options
    if choice in ('1'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        break
    else:
        print("Invalid Input")
