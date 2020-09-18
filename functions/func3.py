# def hello(name="User"):
#     print(f"Hello {name}")
#
#
# hello("David")
# hello("Kumar")
# hello()

# default value arguments should follow non default value
# arguments, not the other way around!
# def say_something(name, color="red"):
#     print(f"My name is {name} and I like {color}.")
#
#
# say_something("pink", "red")
# say_something("xxx")
#
# say_something(color="blue", name="pink")


def foo(a=0, b=0, c=0, d=0):
    if a == 1:
        print("a is 1")
    if b == 1:
        print("b is 1")
    if c == 1:
        print("c is 1")
    if d == 1:
        print("d is 1")


foo(d=1, b=1)
