print()
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
n = int(input("Enter a number: "))
print("sum of numbers from 1 to", n, "is:", sum(n))
print()
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print("Factorial of 5 :", fact(5))
print()