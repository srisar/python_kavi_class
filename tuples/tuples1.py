# tuples are immutable

colors = ("red", "blue", "green")
print(colors)

for c in colors:
    print(c)

print()

print(f"my color is {colors[1]}")

n1 = ("kumar", "david")
n2 = ("babu", "kamala")
all_names = n1 + n2

print(all_names)
