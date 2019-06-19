'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329335446&mode=answer
거스름돈 계산

'''
price = int(input("물건 값?"))
money = int(input("받은 돈?"))
money -= price

money_10000 = money // 10000
money %= 10000

money_5000 = money // 5000
money %= 5000

money_1000 = money // 1000

print("다음과 같이 거슬러주세요:")
if money_10000 > 0 :
    print("10000 x",money_10000)
if money_5000 > 0 :
    print("5000 x",money_5000)
if money_1000 > 0 :
    print("1000 x",money_1000)



