print()
file = open('Students.xlsx' , 'w')
file.write("Name, Student ID\n")
file.write("Kencho, 08250271\n")
file.write("Kinga, 08250273\n")
file.write("Xorji, 08250266\n")
file.write("Soniya, 08250285\n")
file.write("Sharmilla, 08250282\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
search_name = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if search_name.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()