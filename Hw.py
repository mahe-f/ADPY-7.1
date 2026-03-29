# Function 1: Direct multiplication
def multiply1(a, b):
    return a * b

# Function 2: Multiplication using repeated addition
def multiply2(a, b):
    product = 0
    for i in range(b):
        product += a
    return product

# Taking input from user
m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

# Calling functions
print("Multiplication using function 1:", multiply1(m, n))
print("Multiplication using function 2:", multiply2(m, n))