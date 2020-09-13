# list, ordered items, mutable
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits)

# accessing an item of a list

print(fruits[0])
print(fruits[1])

my_fruit = fruits[2]
print(my_fruit)

print()
# accessing items in reverse

print(fruits[-1])
print(fruits[-2])

# range of items
print(fruits[0:3])
print(fruits[3:6])

print()

print(fruits[3:])
print(fruits[:5])

print()
# mutating values

colors = ["red", "green", "blue"]
print(colors)
colors[0] = "yellow"
print(colors)
# colors[5] = "magenta" # this is illegal operation

# add a new item into a list
colors.append("red")
colors.append("magenta")
print(colors)
colors.insert(2, "pink")
print(colors)

# removing an item from a list
colors.remove("pink")
print(colors)

c1 = colors.pop()
print(c1)
print(colors)

c1 = colors.pop()
print(c1)
print(colors)

print()

print("length of colors:", len(colors))

color_to_check = "yellow"

if color_to_check in colors:
    print(f"yes, {color_to_check} is in the list")
else:
    print(f"nope, {color_to_check} is not in the list")

#  looping through a list

for item in colors:
    print(item)

print()

for fruit in fruits:
    print(fruit)

