'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329339185
2. 파일을 입력받아 파일에 가장 많이 쓰인 10개의 단어와 그 횟수를 출력하는 프로그램
-단어와 단어 사이 띄어쓰기 하면 다른 단어임
-영어 대문자 THE랑 소문자 the 같은 단어로 취급
'''
from collections import Counter # collections의 Counter 패키지를 사용하겠다.
word_count = Counter() # word_count라는 이름으로 Counter 패키지를 생성하겠다.

file = open("file.txt","r") # file.txt를 file이라는 이름으로 읽기모드("r")로 연다. 

for line in file: # file의 각 줄을 읽어온다.
    for word in line.lower().split(): # 각 줄을 모두 소문자로바꾸고(lower 메소드) split 메소드를 통해 공백(' ')을 기준으로 모두 분리시킨것을 읽어온다.
        word_count[word] += 1 # word(분리된 각각의 단어)의 Counter를 1씩 증가시킨다.

print("가장 많이 쓰인 10개의 단어와 그 횟수")
for word, cnt in word_count.most_common(10): # word_count에서 Counter가 가장 높은 단어 10개(most_common(10))와 그 횟수를 가져온다.
    print(word,"=>", cnt) # 가져온 단어(word)와 횟수(cnt)를 출력한다.
    
file.close() # open했던 file을 close 해준다.
