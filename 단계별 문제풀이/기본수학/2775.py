t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    zero = [i for i in range(1, n+1)]
    if k == 0:
        print(n)
    for j in range(k):
        for _ in range(1, n):
            zero[_] += zero[_-1] 
    print(zero[-1])
