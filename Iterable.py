mytuple = ("apple", "banana", "cherry")
tmp_arr = []
for i in mytuple:
    if i == 'banana':
        i = 'orange'
    tmp_arr.append(i)
mytuple = tuple(tmp_arr)
print(type(mytuple))

#tuples and arrays/lists are iterable
#tuples can NOT modify in-place