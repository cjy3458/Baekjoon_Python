n1, n2 = map(int, input().split())

for i in range(n1, n2+1):
    count = 0 
    j = 2
    if i > 1:
        while j*j <= i:
            if i % j == 0:
                count += 1
                break
            j += 1
        if count == 0:
            print(i)
