import os 
os.system('clear')
limit = int(input("Enter the sum of n natural numbers : "))
sum = 0
for x in range(limit):
    num = int(input("Enter the " + str(x) + " number : "))
    # print(num)
    sum = sum + num
print("The sum of numbers : ",sum)
# os.system("clear")