n1 = int(input())
n2 = int(input())
pn_list = []

for i in range(n1, n2+1):
    count = 0 
    j = 2
    if i > 1:
        while j*j <= i:
            if i % j == 0:
                count += 1
                break
            j += 1
        if count == 0:
            pn_list.append(i)

if len(pn_list) == 0:
    print("-1")
else:
    print(sum(pn_list))
    print(min(pn_list))

