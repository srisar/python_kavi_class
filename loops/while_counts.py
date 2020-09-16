# version 1
# total = 0
#
# i = 0
# while i < 3:
#     number = input("Enter a number: ")
#     total = total + int(number)
#     i += 1
#
# print("total is", total)


# version 2

total = 0

while True:
    number = int(input("Enter a number: "))
    total = total + number

    if number == 0:
        break

print("total is", total)
