def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number-1)


number = int(input("Enter a number: "))
if number>=0:
 result = factorial(number)
 print(f"The factorial of {number} is {result}")
else:
   print("Please enter a positive number.")

