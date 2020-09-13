fruits = ["apple", "mango", "banana"]
print(fruits)
print()

# new_fruits_list = fruits
#
# print(new_fruits_list)
# new_fruits_list[1] = "kiwi"
#
# print("new fruits list")
# print(new_fruits_list)
#
# print("old fruits list")
# print(fruits)

new_fruits = []
for item in fruits:
    new_fruits.append(item)

print("new fruits:", new_fruits)
new_fruits[0] = "kiwi"

print("old fruits:", fruits)
print("new fruits:", new_fruits)

new_new_list = fruits.copy()
new_new_list[0] = "cherry"
new_new_list[1] = "berry"

print("new new list:", new_new_list)
print("old fruits:", fruits)
print()

# merging two or more list into one big list

f1 = ["apple", "mango"]
f2 = ["banana", "kiwi"]
f3 = ["cherry", "berry"]
# full_list = f1 + f2
# print(full_list)

# for item in f2:
#     f1.append(item)
#
# print("f1:", f1)

f1.extend(f3)
f1.extend(f2)

print("f1:", f1)
f1.reverse()
print("f1 reversed:", f1)
