# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
print("Enter two numbers to define a range:")
while True:
    try:
        num1 = int(input("First number"))
        num2 = int(input("Second number"))

        low = min(num1, num2)
        high = max(num1, num2)
        random_number = random.uniform(low, high)
        #fstrings are cool
        print(f"A random integer between {low} and {high} is {random_number}.")
        break
    except ValueError:
        print("Invalid")
