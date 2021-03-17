print("Program to Find Electricity Bill")

unit_consumed = int(input("Enter the units consumed by customer : "))

if (unit_consumed <= 200):
    charge = 0.5 * unit_consumed
elif (unit_consumed > 200) and (unit_consumed <=400):
    charge = 100 + 0.65 * (unit_consumed - 200)
elif (unit_consumed > 400) and (unit_consumed <= 600):
    charge = 230 + 0.80 * (unit_consumed - 400)    
elif (unit_consumed > 600):
    charge = 390 + 1.0 * ( unit_consumed - 600)


print("Your Electricity Bill for consuming ",unit_consumed, " unit is : ", charge)     