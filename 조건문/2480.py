a, b, c = input().split(" ")
c = int(c)
a = int(a)
b = int(b)

list = [a, b, c]

if a == c and a != b and b != c:
    print(1000 + (a*100))
elif a == b and c != b and a != c:
    print(1000 + (a*100))
elif b == c and a != b and a != c:
    print(1000 + (b*100))
elif a == b and b == c and a == c:
    print(10000+(a*1000))
else:
    print(max(list)*100)
