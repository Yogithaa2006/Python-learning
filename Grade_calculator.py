mark=int(input("Enter a student mark:"))
if(mark>=90):
    print("Grade A")
elif(mark>=75 and mark<=89):
    print("Grade B")
elif(mark>=50 and mark<=74):
    print("Grade C")
else:
    print("Grade F")