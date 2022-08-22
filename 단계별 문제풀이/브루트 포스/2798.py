n, m = map(int, input().split())
result = 0

a = list(map(int, input().split()))

for i in range(n):
    for j in range(i+1, n):
        for _ in range(j+1, n):
            if a[i] + a[j] + a[_] > m:
                continue
            else:
                result = max(result, a[i] + a[j] + a[_])
        

print(result)
