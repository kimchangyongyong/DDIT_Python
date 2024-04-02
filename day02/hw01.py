# 가위바위보를 선택하시오 가위
# 나: 가위
# 컴: 보
# 결과 : 승리
from random import random

# 하고 싶은 방향 : mine과 cpu의 값들의 계산으로 나온 결과 비교로 승/패 가르기 


mine =input("가위 바위 보 중 하나를 선택하시오.")

print("나: ",mine) 

if mine=="바위":
    mine=0
elif mine=="보" :
    mine=1
elif mine=="가위":
    mine=2

    
cpu=int(random()*3)

cpuStr=cpu
if cpuStr == 0 :
    cpuStr = "바위"
elif cpuStr == 1 :
    cpuStr = "보"
else :
    cpuStr = "가위"

print("컴퓨터: ",cpuStr)  

res = int(mine)-cpu

print(res)

if res == 0 :
    print("비겼습니다.")
elif res ==-2 or res == 1 :
    print("이겼습니다.")
else:
    print("졌습니다.")
       
         

    





