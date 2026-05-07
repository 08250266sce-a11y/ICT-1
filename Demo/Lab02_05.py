print()
names_dict = {}
student1_id = (66)
student2_id = (80)
unique_value = (student1_id + student2_id) % 10
print(f"Unique value generated: {unique_value}")

students = {}
while True:
    name = input("Enter student name (or type 'exit' to stop): ").strip()
    if name.lower() == "exit":
        break
    if name == "":
        print(" Warning: Blank name entered. Skipping...")
        continue
    students[name] = 0 

print("\nRegistered Students:")
for student in students.keys():
    print(student)

for student in students.keys():
    print(f"\nQuiz for {student}:")
    score = 0

    # Question 1
    ans1 = int(input(f"Q1: What is {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1

    # Question 2
    ans2 = int(input(f"Q2: What is {unique_value} * 3 = "))
    if ans2 == unique_value * 3:
        score += 1

    # Question 3
    ans3 = int(input(f"Q3: What is {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1

    # Store score
    students[student] = score

    # Step 5: Performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Needs Improvement"
    else:
        performance = "Poor"

    # Step 6: Certificate eligibility
    eligible = "Eligible for Certificate" if score >= 2 else "Not Eligible"

    # Step 7: Warning for score 0
    if score == 0:
        print(" Warning: Score is 0!")

    # Display results
    print(f"Score: {score}")
    print(f"Performance Level: {performance}")
    print(f"Certificate Status: {eligible}")

    # Step 8: Print star pattern
    print("Stars Pattern:")
    if score > 0:
        for i in range(score):
            print("*" * (i + 1))
    else:
        print("")  # Blank for score 0