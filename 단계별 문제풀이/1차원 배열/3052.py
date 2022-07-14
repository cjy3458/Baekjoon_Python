a = []
b = []
c = []

for i in range(10):
    a.append(int(input()))
    b.append(a[i]%42)
    if b[i] not in c:
        c.append(int(b[i]))

print(len(c))