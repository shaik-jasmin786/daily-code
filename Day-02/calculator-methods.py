#using functions

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y
print("Simple calculator")
print("perform operations:")
print("1.Addition:")
print("2.Subtraction:")
print("3.Multiplication:")
print("4.Division:")

choice=input('Enter choice(1/2/3/4):')
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))

if choice=='1':
    print(f"Result:{add(n1,n2)}")
elif choice=='2':
    print(f"Result:{subtract(n1,n2)}")
elif choice=='3':
    print(f"Result:{multiply(n1,n2)}")
elif choice=='4':
    print(f"Result:{divide(n1,n2)}")
else:
    print("Invalid input")


'''#using if-else

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")'''