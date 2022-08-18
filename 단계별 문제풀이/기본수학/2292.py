def isSix(a):
    num = 1
    count = 1
    while a > num:
        num += 6*count
        count += 1
    return count


n = int(input())



print(isSix(n))

'''
num = 1
count = 1

while n > num:
    num += 6*count
    count += 1

print(count)
'''