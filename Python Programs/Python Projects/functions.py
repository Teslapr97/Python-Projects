#Functions in Python for Practice

def add_variables(x,y):
    total = x + y
    return total

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = ""

result = add_variables(x = num1, y = num2)

print(f"The total result is: {result}")
