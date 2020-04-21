class myclass:
    x=5

p1=myclass()
print(p1.x)
p1.x=40
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p2=person("john",34)
#print(p2.name)
#print(p2.age)

class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfn(self):
        print("hello i m "+self.name)
#p3=people("DSF",34)
#p3.myfn()