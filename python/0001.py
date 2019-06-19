'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329335646&page=1#answer1
누진세 계산기
~200kwh : 100/kwh
201~300kwh : 200/kwh
200kwh~ : 300/kwh

'''

def electricity(kwh):
    pay = 0
    if kwh<=200:
        pay = 100 * kwh 
    elif 200 < kwh <= 300:
        pay = 100*200 + 200*(kwh%200)
    else:
        pay = 100*200 + 200*100 + 300*(kwh%300)
    return pay


kwh = int(input("사용량: "))
print("요금 =",electricity(kwh))
