#Multilevel Inheritance

class Base:
    def __init__(self):
        self.i = 10
        self.j = 20
        print("Inside base constructor")


class Derived1(Base):
    def __init__(self):
        Base.__init__(self)
        print("Inside Derrived1 constructor")
        self.x = 30
        self.y = 40

class Derived2(Derived1):
    def __init__(self):
        Derived1.__init__(self)
        print("Inside Derrived2 constructor")
        self.w = 50
        self.z = 60


def main():

    bobj = Base()
    print(bobj.i)
    print(bobj.j)

    dobj1 = Derived1()
    print(dobj1.i)
    print(dobj1.j)
    print(dobj1.x)
    print(dobj1.y)

    dobj2 = Derived2()
    print(dobj2.i)
    print(dobj2.j)
    print(dobj2.x)
    print(dobj2.y)
    print(dobj2.w)
    print(dobj2.z)



if __name__ == '__main__':
    main()
