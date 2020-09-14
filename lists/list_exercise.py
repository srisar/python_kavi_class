# numbers = [1, 2, 3, 4, 5, 6]
# numbers2 = []
#
# for number in numbers:
#     twice = number * 2
#     numbers2.append(twice)
#
# print("number2:", numbers2)

numbers = [32, 76, 99, 12, 56, 21]
odd = []
even = []

for n in numbers:
    if n % 2 != 0:
        odd.append(n)
    else:
        even.append(n)

print(numbers)
print(odd)
print(even)
