'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329345291
카드 포인트 적립하기
'''
def Point(p_type, price):
    if p_type=="1":
        per = 0.012
    elif p_type=="2":
        per = 0.02
    elif p_type=="3":
        per = 0.018
    elif p_type=="4":
        per = 0.015
    return int(price*per)

current_point = 0
while 1:
    p_type = input("어떤 상품을 구매하셨나요?(화장품(1),커피(2),도서(3),의류(4)):")
    price = int(input("구입 가격은 얼마인가요?"))
    
    current_point += Point(p_type,price)
    
    print("적립된 포인트는 "+str(current_point)+"입니다\n")
