#출력할 단수를 입력하세요
#2*1=2
#2*2=4
#.
#.
#2*9=18

a=input("출력할 단수를 입력하세요")
res = 1
for i in range(1, 9+1) :
    res=int(a)*i
    print("{}*{}={}".format(a,i,res))
    # print("{}*{}={}".format(a,i,int(a)*i))
    

    