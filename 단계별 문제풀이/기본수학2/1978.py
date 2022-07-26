n = int(input())
PN = 0


for i in range(n):
    a = int(input())
    count = 0
    for j in range(1, a+1):
        if a % j == 0:
            count += 1
        if count == 2:
            PN += 1
    
print(PN)
