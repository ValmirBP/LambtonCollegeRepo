# UML

'''
1) Name : Monitor
2) Parameter(Attributes) : size, price, brand...
3) On() Off()

*** What is the benefit of using object-oriented database (classes) over
DBMS ?

# classes name has to start with capital letter
# override a function : >
'''

class Monitor :
    def __init__(self, size, price, brand):
        self.size = size
        self.price = price
        self.brand = brand

    def __str__(self):
        return f'Monitor ---> {self.brand}, size : {self.size}, price : $ {self.price}'

    def add(self):
        print('hello')

# Constructor after creating the instance (object) it will pass it to a dunder method called
#  initializer for initialization. All the classes in python extends from a super class
# called objects --> (object class is the collection of functions method which helps you
# manipulate you class better!
# constructor ---> create an instance(object) out of the class
m1 = Monitor(20, 1000, "LG") # what we call a function that has same name as a class
# you can only use constructor once! when you creating an object
m2 = Monitor(17, 870, "Samsung")
print(m1) # string representation of an object!
print(f'Monitor ---> {m1.brand}, size : {m1.size}, price : $ {m1.price}')
print(f'Monitor ---> {m2.brand}, size : {m2.size}, price : $ {m2.price}')
print(hex(m1.__hash__())) # return a memory location hashcode()
print(m1.__str__()) # the dunder __str__() return a string representation of an object!
# when you call m1 by default call the dunder function __str__()
print(m2)

