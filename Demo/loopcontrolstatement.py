print()
for i in range(4):
    if i == 2:
        break
    print(i)
print("Loop ended")
print()

for i in range(4):
    if i == 2:
        continue
    print(i)
print("Loop ended")
print()
   #Exercise(Q.1)
i = 10
while i >= 1:
    print(i)
    i -= 1
print("times up!")
print()
# Question 2
i = 0
while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    i += num
print("Total sum:", i)
# Question 3
correct_username = "admin"
correct_password = "1234"
attempts = 3
while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("login successful")
        break
    else:
        attempts -= 1
        print("Incorrect credentials. Attempts left:", attempts)
if attempts == 0:
    print("account locked")

