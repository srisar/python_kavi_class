# defining a function: this will not execute the function
def hello_world():
    print("I'm just sayin' hello!")


# calling a function
# function definition should be above the calling
hello_world()
hello_world()
hello_world()


# functions with arguments
def say_hello(name):
    print(f"Hello {name}")


say_hello("David")  # name=David
say_hello("Babu")  # name=Babu
