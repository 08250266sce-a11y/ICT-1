print()
def fun1(x, y):
    if x == 0:
        return y
    else:
        return fun1(x-1, y +x)
x = int(input("Enter the number for x : "))
y = int(input("Enter the number for y : "))
result = fun1(x, y)
print("Result : ", result)
print()