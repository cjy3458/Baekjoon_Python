c = int(input())


for i in range(c):
    count = 0
    result = 0
    a = list(map(int, input().split(" ")))
    aver = sum(a[1:])/a[0]
    for j in range(1, len(a)):
        if a[j] > aver:
            count += 1
    result = count/a[0]*100
    print("{:.3f}%".format(result))
