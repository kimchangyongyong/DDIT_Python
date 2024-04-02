# 홀/짝을 선택하시오 홀
# 나: 홀
# 컴: 홀
# 결과 : 승리 
from random import random

mine=input("홀/짝을 선택하시오")
print("mine:",mine)

cpu=random()

if cpu>0.5 :
    cpu="홀"
else :
    cpu="짝"

print("cpu:",cpu)    

if cpu==mine :
    print("결과 : 승리")
else :
    print("결과 : 패배 ")  






