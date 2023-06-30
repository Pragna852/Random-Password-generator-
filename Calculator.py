import time

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2



while True:
    print("Operations available:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice from  above options: ")

    if choice == '5':
        print(" Program Exit.")
        
        break

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = addition(num1, num2)
        print("Addition:", result)
        
        time.sleep(1)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtraction(num1, num2)
        print("Subtraction:", result)
        
        time.sleep(1)
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiplication(num1, num2)
        print("Multiplication:", result)
        
        time.sleep(1)
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = division(num1, num2)
        print("Division:", result)
        time.sleep(1)
    else:
        print("Input is out of range! Try 1-5")
        
        time.sleep(1)