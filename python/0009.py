'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329484894
띄어쓰기를 기준으로 파일에 있는 단어 별 빈도 계산한 다음에 오름차순으로 정렬해 출력하는 것 좀 풀어주세요 부탁합니다
'''
file = open("file.txt","r")

word_list={}
for line in file:
    for word in line.lower().split():
        if word in word_list:
            word_list[word]+=1
        else:
            word_list[word]=1

word_list = sorted(word_list.items(),key=lambda x:x[1],reverse=True)

idx = 0
for word,count in word_list:
    idx += 1
    print("%s => %d"%(word,count))
    if idx==10:
        break
