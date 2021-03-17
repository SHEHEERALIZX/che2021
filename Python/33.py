# python program to print fibinocci series of upto particular number
nterms = int(input("How many terms? "))
count = 0
num1, num2 = 0, 1
while count < nterms:
    print(num1)
    nth = num1 + num2
    # update values
    num1 = num2
    num2 = nth
    count = count + 1
    