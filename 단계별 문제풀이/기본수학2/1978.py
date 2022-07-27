n = int(input())
num = map(int, input().split())
PN = 0 

for i in num:
    count = 0 
    j = 2
    if i > 1:
        while j*j <= i:
            if i % j == 0:
                count += 1
                break
            j += 1
        if count == 0:
            PN += 1

print(PN)






'''
n = int(input())
num = map(int, input().split())
PN = 0

for i in num:
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            PN += 1

print(PN)

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
'''