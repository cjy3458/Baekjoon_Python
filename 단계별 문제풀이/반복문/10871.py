a, b = input().split(" ")
a = int(a)
b = int(b)

c = list(map(int, input().split(" ")))

for i in range(a):
    if c[i] < b:
        print(c[i], end=" ")