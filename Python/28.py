import os 
os.system('clear')
print("Program to find factorial of a number :\n \n")

num = int(input("Enter the number to print factorial of the number : "))
fact = 1
for x in range(1,num + 1):
    fact = fact * x
print("Factorial Of a number : ",fact)