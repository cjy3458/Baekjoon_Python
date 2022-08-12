import math

def isPrime(_):
    a = math.sqrt(_)
    if (_ < 2):
        return False
    for i in range(2, int(a)+1):
        if (_ % i == 0):
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    for a in range(n // 2, 0, -1):
        if isPrime(a) and isPrime(n - a):
            print(a, n - a)
            break