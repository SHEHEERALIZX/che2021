limit = int(input("Enter the Limit to print N natural numbers their squares and cubes : "))
for x in range(1,limit+1):
    sqr = x * x 
    cube = x * x * x
    print('Number   || ',x, 'square is : ',sqr, "|| cube is : ",cube)