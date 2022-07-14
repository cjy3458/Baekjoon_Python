n = int(input())

for i in range(n):
    a = input()
    sum = 0
    count = 0
    for j in list(a):
        if j == 'O':
            count = count + 1
            sum = sum + count
        else:
            count = 0
    print(sum)
