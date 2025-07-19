try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
except ValueError:
    print("Enter valid integers for a and b.")
    exit()

print("Choose an operation:")
print("Press + for addition")
print("Press - for subtraction")
print("Press * for multiplication")
print("Press / for division")

o = input("Enter operation: ")

match o:
    case "+":
        print(f"The result is: {a + b}")
    case "-":
        print(f"The result is: {a - b}")
    case "*":
        print(f"The result is: {a * b}")
    case "/":
        try:
            print(f"The result is: {a / b}")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")


