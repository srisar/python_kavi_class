def add(a, b):
    return a + b


x = add(1, 2)
y = add(2, 3)

print("x:", x)
print("y:", y)
print(add(3, 6))

z = add(add(1, 2), add(6, 7))
print("z:", z)
