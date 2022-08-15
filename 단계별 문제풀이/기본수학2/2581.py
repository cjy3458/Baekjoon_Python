n1 = int(input())
n2 = int(input())
pn_list = []

'''
def isPrime(a):
    if a < 2:
        return False
    else:
        for j in range(2, a):
            if a % j == 0:
                return False
    return True
'''

for i in range(n1, n2+1):
    count = 0 
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            pn_list.append(i)

if len(pn_list) == 0:
    print("-1")
else:
    print(sum(pn_list))
    print(min(pn_list))

