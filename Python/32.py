# program to find reverse of a number using while loop\


num = int(input("Enter the number to output the reverse of a number  :"))

sum = 0 

while num > 1:
    m = num % 10
    sum = sum + m 
    num = int(num / 10)
print(sum)    
