marks1 = float(input("Enter the marks of first subject: "))
marks2 = float(input("Enter the marks of second subject: "))
marks3 = float(input("Enter the marks of third subject: "))
Average = (marks1 + marks2 + marks3) / 3
print("Averge:",Average)
if (Average >= 90 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: A")
elif(Average >= 80 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: B")
elif(Average >= 70 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: C")
elif(Average >= 60 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: D")
elif(Average >= 50 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: E")
else:
    print("You need to work harder")