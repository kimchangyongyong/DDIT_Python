from day03.ooptest01 import Animal
from day03.ooptest01 import Human
class Ooptest:
    ani=Animal()
    print("name:",ani.name)
    ani.named("전청조")
    print("name:",ani.name)
    
    hum=Human()
    print("asset:",hum.asset)
    hum.goldspoon(10000000000)
    print("asset:",hum.asset)