def jack(_):
    if _ <= 1:
        return _
    return jack(_-1) + jack(_-2)


n = int(input())

print(jack(n))