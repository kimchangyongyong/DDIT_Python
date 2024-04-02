class Animal:
    def __init__(self):
        self.name = ""
        
    def named(self,name):
        self.name = name
        
    def __str__(self):
        return "[Animal][name]:"+self.name
    
    def __del__(self):
        pass

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.asset=0
    
    def goldspoon(self, asset):
        self.asset = asset
      

if __name__ == "__main__" :
    hum=Human()
    print("asset:",hum.asset)
    print("name:",hum.name)
    hum.named("전청조")
    hum.goldspoon(10000000000)
    print("asset:",hum.asset)
    print("name:",hum.name)

# if __name__ == "__main__":   
#     ani=Animal()
#     print(ani)
#     ani.named("전청조")
#     print(ani)
#
#     hum=Human()
#     print(hum)
#     hum.goldspoon(10000000000)
#     print(hum)
