import os 
os.system('clear')

limit = int(input("Enter the limit :"))

mult = int(input("Enter the table do you want :"))

for x in range(1,limit + 1):
    result = x * mult
    print(x , "*" , mult , "=" , result)