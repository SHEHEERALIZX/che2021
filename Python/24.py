import os 
os.system('clear')
limit = int(input("Enter the sum of n natural numbers : "))
sum = 0
for x in range(1,limit+1):
    sum = sum + x
print("The sum of numbers upto",x,"is : ",sum)