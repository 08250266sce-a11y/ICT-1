print()
name = str(input("Enter your name: "))
days_borrowed = int(input("Enter the number of days the book was borrowed: "))
days_late = int(input("Enter the number of days late to return: "))  
print()
if days_borrowed > 30:
    print("Warning: Libary privileges may be restricted")
    print()
    #quit()
else:
    print("Notice: No warning")
    print()
if days_late<=0:
    print("Total Fine: You have no due")
elif 1<=days_late<=5:
    due1=(days_late * 5)
    print("Total Fine: You have Nu.",due1," due to pay")
elif 6<=days_late<=10:
    due2 = (days_late * 10)
    print("Total Fine: You have Nu.",due2,"due to pay")
else:
    days_late<=10
    due3 = (days_late * 20)
    print("Total Fine: You have Nu.",due3,"due to pay")   
print()  