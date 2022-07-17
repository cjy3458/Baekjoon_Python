num = int(input())
count = 0

for i in range(1, num+1):
    number = list(map(int, str(i)))
    if i < 100:
        count += 1
    elif number[0] - number[1] == number[1] - number[2]:
        count += 1
        #print(number) --> 한수를 전부 알 수 있음
        

print(count)