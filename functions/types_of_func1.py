# Types of functions
# 1. With returnable value
# 2. Without returnable value (procedure)

#

#
# 1. With returnable value
def add(a, b):
    return a + b


x = add(3, 4)


# add(1,2) = x # cant do this!


# 2. Without returnable value
def sayHello():
    print("saying hello!")
    print("saying goodbye!")


sayHello()
