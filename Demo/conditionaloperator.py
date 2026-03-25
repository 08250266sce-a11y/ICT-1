marks1 = float(input("Enter the marks of first subject: "))
marks2 = float(input("Enter the marks of second subject: "))
marks3 = float(input("Enter the marks of third subject: "))
average = (marks1 + marks2 + marks3) / 3
if (average >= 90 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: A")
elif(average >= 80 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: B")
elif(average >= 70 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: C")
elif(average >= 60 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: D")
elif(average >= 50 and marks1 >= 50 and marks2 >= 50 and marks3 >= 50):
    print("Grade: E")
else:
    print("You need to work harder")