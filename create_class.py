class Person:
    def __init__(self, name, age, arr):
        self.name = name
        self.age = age
        self.arr = arr

    def Greet(self):
        print(f'Hello {self.name}')

    def PrintArr(self):
        for x in self.arr:
            print(x, end=' ')
#Array is iterable

my_arr = [1,2,3]

per_obj = Person("Vincent", 18, my_arr)
per_obj.PrintArr() 