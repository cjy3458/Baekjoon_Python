def jack(_):
    a = 1
    for i in range(2, _+1):
        a *= i
    return a




n = int(input())



print(jack(n))