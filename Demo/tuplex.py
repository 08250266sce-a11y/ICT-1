my_tuple = ("Hello", 123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
a, b = my_tuple
print(b)
new_tub = tuple(a)
print(new_tub)
concatenated_tuple = my_tuple + new_tub
print(concatenated_tuple)
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1])
#del my_tuple
#print(my_tuple)
print(concatenated_tuple[:2]+concatenated_tuple[2:][::-1])
#n = concatenated_tuple[2:7:4] *same result as step 19
#print(n[::-1])
#print(concatenated_tuple[6:1:-4]) *same result as step 19
print(concatenated_tuple[2:7:4][::-1]) # print(concatenated_tuple[::-1])
print()