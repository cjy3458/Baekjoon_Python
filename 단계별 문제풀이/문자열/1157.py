word = input().lower() # 입력받은 단어를 모두 소문자로 변환
word_list = list(set(word)) # 입력받은 단어 중 중복되는 알파벳을 제거하고 리스트로 작성
num = [] # 각 알파벳 개수를 넣을 리스트 선언

for i in word_list: # 중복없는 단어리스트를 for문으로 돌림
    number = word.count(i) # number는 단어리스트에 알파벳이 단어의 들어간 횟수
    num.append(number) # 횟수를 선언안 리스트에 입력

if num.count(max(num)) >= 2: # 혹시 num에 가장 큰 값을 세었을때 2개 이상이라면
    print("?")
else:
    print(word_list[num.index(max(num))].upper())

