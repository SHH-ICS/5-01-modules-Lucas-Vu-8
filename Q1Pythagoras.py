# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
while True:
    try:
        a = float(input("enter"))
        b = float(input("enter"))
        #btw .sqrt is square root
        c = math.sqrt(a**b + b**2)
        print(c)
        break
    except ValueError:
        print("Invalid")
