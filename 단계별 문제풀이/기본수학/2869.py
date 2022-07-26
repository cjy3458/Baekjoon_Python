a,b,v = map(int,input().split())
k = (v-b)/(a-b)
if k == int(k): 
    print(int(k))
elif k != int(k):
    print(int(k)+1)

'''
while v > h:
    h = h + a
    if h >= v:
        day += 1
        break
    h = h - b
    day += 1

print(day)


# a = 올라가는 미터 b = 미끄러지는 미터 v = 도달해야되는 높이
# 0 = 0 + 2, 2 = 2 - 1
a * k - bk - b >= v
'''