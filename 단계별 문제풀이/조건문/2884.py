a, b = input().split(" ")

a = int(a)
b = int(b)

if b >= 45:
    print(a, b - 45)
elif a > 0 and b < 45:
    print(a-1, b + 15)
elif a == 0 and b < 45:
    print(23, b+15)
