import math

def isPrime(_):
    a = math.sqrt(_)
    if (_ < 2):
        return False
    for i in range(2, int(a)+1):# 2부터 n의 제곱근까지만 나눠서 시간 단축
        if _ % i == 0:
            return False
    return True


n1, n2 = map(int, input().split())

for i in range(n1, n2+1):
    if isPrime(i):
        print(i)




'''
n1, n2 = map(int, input().split())

for i in range(n1, n2+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            print(i)
'''