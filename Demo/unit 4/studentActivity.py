print()
file = open('Students.xlsx' , 'w')
file.write("Name, ID\n")
file.write("Sonam, 10713002876\n")
file.write("Kinga, 10706003427\n")
file.write("Dorji, 11105002924\n")
file.write("Tobgay, 1151002253\n")
file.write("Tshering, 11105002899\n")
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