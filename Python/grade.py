mark1 = int(input("Enter the mark obtained in Maths :"))
mark2 = int(input("Enter the mark obtained in English :"))
mark3 = int(input("Enter the mark obtained in Chemsitry :"))
mark4 = int(input("Enter the mark obtained in Physics :"))



avg = (mark1 + mark2 + mark3 + mark4) / 4

if (avg >= 90):
    print("outstanding")

elif (avg >= 80) and (avg < 90):
    print("Very Good") 

elif (avg >= 70) and (avg < 80):
    print("Good") 

elif (avg >= 60) and (avg < 70):
    print("Average") 

elif (avg >= 50) and (avg < 60):
    print("Satisfactory") 


else :
    print("\n")
    print("You Failed")

    
       