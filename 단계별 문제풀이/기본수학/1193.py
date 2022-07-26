n = int(input())
line = 1
i = 0

while n > i + line:
    i += line
    line += 1

a = n - i

if line % 2 == 0:
    print("%d/%d" % (a, line-a+1))
elif line % 2 == 1: 
    print("%d/%d" % (line - a + 1, a))





'''
1/1
1/2 2/1
3/1 2/2 1/3
4/1 3/2 2/3 1/4

=> 4-1/1+1 4-2/1+2

1. n번째 줄에는 n개의 항이 있다
2. n번째 줄의 i번째 항 n-i+1/1+i-1
3. 홀수항 1+i-1/n-i+1

sum =0
i=1
while(sum + i < n):
    sum += i
    i += 1
'''