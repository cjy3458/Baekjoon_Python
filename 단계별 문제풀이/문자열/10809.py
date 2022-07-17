s = input()
alpha = list(range(97,123)) # 소문 아스키코드 범위

for _ in alpha:
    print(s.find(chr(_))) # find함수의 적합한 문제 없을 시 -1 출력
