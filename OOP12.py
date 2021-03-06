#Multiple Inheritance

class Base1:
    def __init__(self):
        print("Inside Base1 constructor")
    def fun(self):
        print("Base1 fun")


class Base2:
    def __init__(self):
        print("Inside Base2 constructor")
    def fun(self):
        print("Base2 fun")


class Derived(Base1,Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("Inside Derived constructor")



def main():

    dobj = Derived()
    dobj.fun()


if __name__ == '__main__':
    main()
