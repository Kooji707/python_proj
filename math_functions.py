'''
import math

x = 3.9
print(math.ceil(x))
print(math.floor(x))
'''

#mylist = (1, 3, 9)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total
x_y = multiply(1, 3, 9)
print(x_y)