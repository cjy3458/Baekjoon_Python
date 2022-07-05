a, b = input().split(" ")
c = int(input())
a = int(a)
b = int(b)

a += c // 60
b += c % 60

if b >= 60 :
    a+=1
    b-=60

if a >= 24 :
    a-=24

print('%d %d' % (a,b))
