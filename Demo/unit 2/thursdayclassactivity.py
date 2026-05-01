print()
def print_pattern(n):
    # Base case
    if n == 0:
        return
    
    # First recurse down
    print_pattern(n - 1)
    
    # Then print stars after returning
    print("* " * n)

# Example usage
n = 4 #int(input("Enter the number for n value: "))
print_pattern(n) 
print()