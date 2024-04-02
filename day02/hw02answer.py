from random import random

com = int(random()*99)+1

for i in range(10):
    mine = input("숫자를 입력하세요")
    imine = int(mine)
    if com > imine :
        print("{} up입니다.".format(mine))
    elif com < imine :
        print("{} down입니다.".format(mine))
    else :
        print("{} 정답입니다.".format(mine))
        break
        