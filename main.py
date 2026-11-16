
# main.py

from calculator import add, subtract, multiply, divide

# Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
print("\nCalculator Results")

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))

try:
    print("Division:", divide(num1, num2))
except ValueError as error:
    print("Division Error:", error)
