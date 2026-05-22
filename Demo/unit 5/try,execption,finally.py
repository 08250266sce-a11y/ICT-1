print()
try: #Runs the code
    n = float(input("Enter a number: "))
    res = 100/n
except ZeroDivisionError: #Handles the error when dividing by zero
    print("you can't divide by zero!")
except ValueError: #Handles the error when the input is not a valid number
    print("Enter a valid number!")
except: #Handles any other unexpected errrors
    print("An unexpected error occurerd.")
else: #Executes if there are no execptions
    print("Result is", res)
finally: #Executes all the time, regardless of execptions.
    print("Execution complete.")
print()