def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Simple Calculator")
num1 = float(input("Enter first value "))
num2 = float(input("Enter second value "))

print("Select option: 1 (add), 2 (subtract), 3 (multiple), 4 (divide)")
choice = input("Your choice (1/2/3/4): ")

if choice == '1':
    print("Result:", add(num1, num2))

elif choice == '2':
    print("Result:", subtract(num1, num2))

elif choice == '3':
    print("Result:", multiply(num1, num2))

elif choice == '4':
    print("Result:", divide(num1, num2))

else:
    print("No Choice")
