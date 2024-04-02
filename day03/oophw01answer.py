class Xi:
    def __init__(self):
        self.money= 1000
        
    def spend(self, cost):
        self.money-= cost
        
class Putin:
    def __init__(self):
        self.cnt_nuclear = 10000
        
    def war(self):
        self.cnt_nuclear-= 1
        
class Minkyu(Putin,Xi) :
    
    def __init__(self):
        Putin.__init__(self)
        Xi.__init__(self)
        

if __name__ == '__main__':
    mk = Minkyu()
    print(mk.money)
    print(mk.cnt_nuclear)
    mk.spend(5)
    mk.war()
    print(mk.money)
    print(mk.cnt_nuclear)
    

        