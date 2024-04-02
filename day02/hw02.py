#com=(1~99사이의 숫자) ex)50
#숫자를 입력하시오 ex)40
#up~~~, 맞으면 정답입니다. 출력 
#for문 사용 10번만/ 10번 초과하면 끝
from random import random

# 원하는 방향: random사용 1~99의 숫자 생성, for문 돌리기 등

com=int(random()*99+1)
# print(com)


for i in range(1,10+1):
    
    no = input("숫자를 입력하세요.")
    
    if com>int(no) :
        print("-"*30)
        print(no+"보다 up")
        print(str(i)+"/10번 시도했습니다.")
        print("-"*30)
    elif com==int(no):
        print("-"*30)
        print("\t*정답입니다.*")
        print("-"*30)
        break
    else :
        print("-"*30)
        print(no+"보다 down")
        print(str(i)+"/10번 시도했습니다.")
        print("-"*30)
    
    if i == 10 :
        print("도전 기회를 다 소진했습니다.")
        print("정답은"+str(com)+"입니다.")