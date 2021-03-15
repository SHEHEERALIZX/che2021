import os 
os.system('clear')
print("Program to find the sum of squares of any numbers  \n\n")
limit = int(input("Enter the limit : "))
sum = 0
for x in range(limit):
    num = int(input("Enter the " + str(x) + " number : "))
    # print(num)
    # square = num * num
    sum = sum + (num * num)
print("The sum of squares of numbers : ",sum)
# os.system("clear")