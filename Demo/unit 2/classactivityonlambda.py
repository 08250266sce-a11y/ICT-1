# Lambda function
print()
check_number = lambda num: "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")
# Taking input from user
num = int(input("Enter a number: "))
# Using the lambda function
print("The number is:", check_number(num))
print()