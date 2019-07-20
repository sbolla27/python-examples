def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except:
        print("You cannot divide by zero")



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4):"))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multi(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")