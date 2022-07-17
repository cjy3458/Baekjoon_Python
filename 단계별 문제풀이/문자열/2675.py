t = int(input())

for i in range(t):
    r, s = input().split(" ")
    result = ""
    for x in s:
        result += int(r)*x
    print(result)