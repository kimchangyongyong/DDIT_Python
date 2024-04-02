class Xi:
    def __init__(self):
        self.money= 1000
        
    def spend(self, cost):
        self.money-= cost
class Putin:
    def __init__(self):
        self.cnt_nuclear = 10000
        
    def war(self, cnt_nuclear): #1ㄱㅐ씩 감소하는 것을 만들어야 했음 
        self.cnt_nuclear-= cnt_nuclear
        
pt = Putin()
pt.war(1200)
print("푸틴의 남은 핵:",pt.cnt_nuclear)

        