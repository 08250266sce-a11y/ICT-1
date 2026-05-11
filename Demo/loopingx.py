#name = input("Enter your name: ")
#for i in name:
   # print(i)
#print()
li = ["python programming","python fundamental","python interview questions"]
for x in li:
    print(x)
print()
lenli = len(li)
for x in range(lenli):
    print(li[x])
print()
my_tuple = tuple(li)
for x in (my_tuple):
    print(x)
print()
my_set = set(li)
for x in (my_set):
    print(x)
print()
tup = ("John Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)
print()
set1 = {10, 30, 20}
for x in set1:
    print(x)
print()
BookDetails = dict({"Python Programming":"John Smith", "Python Fundamentals":"Alice Johnson", "Python Interview Questions":"Jane Doe"})
for key in BookDetails:
    print(key, BookDetails[key])
print()

for i in range(1,4): #outer loop iterates from 1 to 3
    for j in range(i): #inner loop iterates from 0 to i-1
        print(f"outer loop iteration {i}, inner loop iteration {j+1}")
print()
for i in range(4):
    for j in range(i):
        print("*", end = " ")
    print()
print()