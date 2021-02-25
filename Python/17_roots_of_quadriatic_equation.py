import math
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))


disc = (num2 * num2 - 4 * num1 * num3)

if (disc < 0 ):
    print(" Roots are imaginary ")
elif (disc == 0):
    x1 = -num2 / 2 * num1
    print(x1)
else :
    x1 = (-num2 + math.sqrt(disc)) / 2 * num1    
    x2 = (-num2 - math.sqrt(disc)) / 2 * num1   
    print(x1)
    print(x2)



