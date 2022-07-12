a = int(input())
b = int(input())
c = int(input())

list_1 = list(str(a*b*c))

for i in range(10):
    print(list_1.count(str(i)))
