from math import sqrt,log,sin

number = float(input("Enter a number: "))
if number>0:
    print(f"Square root: {sqrt(number)}")
    print(f"Logarithm: {log(number)}")
    print(f"Sine: {sin(number)}")
else:
    print("Please enter a positive number greater than 0.")