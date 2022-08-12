import math

def isPrime(_):
    a = math.sqrt(_)
    if (_ < 2):
        return False
    for i in range(2, int(a)+1):
        if (_ % i == 0):
            return False
    return True

all = list(range(2, 246912))
pn = []

for i in all:
    if isPrime(i):
        pn.append(i)

while 1:
    count = 0
    a = int(input())
    if a == 0:
        break
    for j in pn:
        if a < j <= 2*a:
            count += 1
    print(count)

'''
import math

def isPrime(_):
    a = math.sqrt(_)
    if (_ < 2):
        return False
    for i in range(2, int(a)+1):
        if (_ % i == 0):
            return False
    return True


while 1:
    count = 0
    a = int(input())
    if a == 0:
        break
    count = 0
    for j in range(a+1, (2*a)+1):
        if (isPrime(j)):
            count += 1
    print(count)
'''
