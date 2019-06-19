'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329444388
'''

def findBMI(weight, height):
    return weight/((height/100)**2)


weight = int(input("체중?"))
height = int(input("키?"))

result = findBMI(weight,height)
if result<20 :
    print("저체중")
elif result <25:
    print("정상")
elif result < 30:
    print("과체중")
else:
    print("비만")
