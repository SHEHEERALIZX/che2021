
# program to find the sum of digits


num = int(input("Enter the number to find of sum of digits :"))

sum = 0 

while num > 1:
    m = num % 10
    sum = sum + m 
    num = int(num / 10)
print(sum)    
