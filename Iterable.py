mytuple = ("apple", "banana", "cherry")
tmp_arr = []
for i in mytuple:
    if i == 'banana':
        i = 'orange'
    tmp_arr.append(i)
mytuple = tuple(tmp_arr)
print(type(mytuple))