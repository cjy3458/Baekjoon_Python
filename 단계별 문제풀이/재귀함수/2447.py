def jack(a):
    global star

    if a == 3:
        star[0][:3] = star[2][:3] = [1]*3
        star[1][:3] = [1, 0, 1]
        return
    
    n = a//3
    jack(a//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(n):
                star[n*i+k][n*j:n*(j+1)] = star[k][:n]

num = int(input())

star = [[0 for i in range(num)] for i in range(num)]

jack(num)

for i in star:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()