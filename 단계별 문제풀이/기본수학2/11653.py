n = int(input())

a = 2

while n != 1:
    if n % a != 0:
        a += 1
    else:
        print(a)
        n //= a
