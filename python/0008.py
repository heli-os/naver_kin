'''
https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10402&docId=329483033#answer1
'''

u_feet = int(input("Enter number of feet: "))
u_inches = int(input("Enter number of inches: "))

tmp_inches = u_feet*12 + u_inches
u_cm = tmp_inches * 2.54

print("%d ft %d in = %.2f cm"%(u_feet,u_inches,u_cm))
