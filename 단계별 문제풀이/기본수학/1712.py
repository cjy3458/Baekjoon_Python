a, b, c = map(int, input().split(" "))
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)

'''a, b, c = map(int, input().split(" "))

print(a, b, c)
count = 0


for i in range(b):
    count += 1
    if i*c >= a + (i*b):
        print(count)
        break

for i in range(b):
    if i*c < a + (i*b):
        count = 0
        


if count == 0:
    print("-1")
'''