mass1 = int(input("Enter Mass 1 :"))
mass2 = int(input("Enter Mass 2 :"))
gravity = int(input("Enter Gravity  :"))


tension = (2 * mass1 * mass2/(mass1 + mass2)) * gravity

print("Tension of steel  : ",tension)