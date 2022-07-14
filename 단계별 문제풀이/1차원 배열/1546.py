n = int(input())
new_list = list(map(int, input().split(" ")))
max_num = max(d)

for i in range(n):
    new_list[i] = (new_list[i]/max_num)*100

print(sum(new_list)/n)