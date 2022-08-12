def isPrime(a):
    if (a<2):
        return False
    for i in range(2, a):
        if(a%i == 0):
            return False
    return True

n = int(input())
num = map(int, input().split())
PN = 0 

for i in num:
    if (isPrime(i)):
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
'''




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