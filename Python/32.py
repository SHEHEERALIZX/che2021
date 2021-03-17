# program to find reverse of a number using while loop\


num = int(input("Enter the number to output the reverse of a number  :"))

# print(num[::-1])

r = ''
reverse = 0
while num + 1 > 1:
    rem = num % 10
    reverse = reverse * 10 + rem
    num = int(num / 10)
    # print(reverse)
    # print(num)
print(reverse)    
