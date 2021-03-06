#Multiple Inheritance

class Base1:
    def __init__(self):
        self.i = 10
        self.j = 20
        print("Inside Base1 constructor")


class Base2:
    def __init__(self):
        print("Inside Base2 constructor")
        self.x = 30
        self.y = 40

class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived constructor")
        self.w = 50
        self.z = 60


def main():

    dobj = Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.w)
    print(dobj.z)



if __name__ == '__main__':
    main()
