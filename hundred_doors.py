"""x = 0
list = []
while x < 100:
    list[x] = list.append(0)
    x = x + 1"""
list = [0] * 100
for a in range(1, 101):
    for b in range(100):
        if (b + 1) % a == 0:
            if list[b] == 0:
                list[b] = 1
            else:
                list[b] = 0
print("The following doors are open: ", end="")
for c in range(100):
    if list[c] == 1:
        print(c + 1, "", sep=', ', end='')
