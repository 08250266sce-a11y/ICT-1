no_of_students = int(input("Enter the number of students: "))
i = 1
students_names = {}
while i <= no_of_students:
    name = input("Enter the name of the student: ")
    print("The name of the student {} is {}".format(i, name))
    i += 1
    students_names[i] = name
print(students_names) 
while True:
    print("This is an infinite loop. Press Ctrl + c to stop it.")