n = int(input())

num = 1
count = 1

while n > num:
    num += 6*count
    count += 1

print(count)