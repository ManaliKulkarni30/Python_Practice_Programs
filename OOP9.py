#Inheritance

class Base:
    def __init__(self):
        self.i = 11
        self.j = 21
        print("Inside base constructor")

    def fun(self):
        print("Inside base fun")

    def gun(self):
        print("Inside base gun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Inside Derrived constructor")
        self.x = 30
        self.y = 40

    def sun(self):
        print("Inside derived sun")

    def gun(self):
        print("Inside Derived gun")

def main():

    bobj = Base()
    print(bobj.i)
    print(bobj.j)
    bobj.fun()
    bobj.gun()

    dobj = Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.sun()
    dobj.gun()
    dobj.fun()

if __name__ == '__main__':
    main()
