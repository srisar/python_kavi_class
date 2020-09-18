def print_fruits(a_list):
    index = 1
    for item in a_list:
        print(f"{index}.{item.title()}")
        index = index + 1


fruits = ["banana", "mango", "kiwi", "strawberry"]
names = ["david", "babu", "bala", "kamala", "rajesh"]
# 1.Banana
# 2.Mango
# 3.Kiwi

# print_fruits(fruits)
print_fruits(names)

# 1,1,2,3,5,8,13...
