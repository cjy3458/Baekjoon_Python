num_set = set(range(1, 10000))
notself = set()
for num in num_set:
    for _ in str(num):
        num += int(_) # d(n)을 거쳐 나온 값이기 때문에 셀프넘버가 아님 
    notself.add(num)
    
selfnum = num_set - notself # set의 -를 이용한 차집합 구하기
for self in sorted(selfnum): # sorted는 순서대로 정렬하는 함수
    print(self)




