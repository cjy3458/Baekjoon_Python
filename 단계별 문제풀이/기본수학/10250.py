t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    num = c//a + 1
    floor = c % a
    if c % a == 0:  # h의 배수이면,
        num = c//a
        floor = a
    print(f'{floor*100+num}')



'''
t = int(input())
g = 1 # 층
d = 1 # 호수
e = 1 #번째
# a = 층 b = 호 c = 몇번째
for i in t:
    a, b, c = map(int, input().split())
    while e <= c:
        if e == c:
            print(g*100 + d)
        elif e < c:
            e += 1
            while g <= a:
                g += 1
                if g == a:
                    
                    d += 1
'''

