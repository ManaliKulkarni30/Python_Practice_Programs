
class Demo:
    x = 10#Class variable
    y = 20
    def __init__(self):
        print("Inside constructor")
        self.i = 30 #Instance variable
        self.j = 40

    def __del__(self):
        print("Inside Destructor")

    def fun(self):
        print("Inside fun")

def main():
    obj1 = Demo()#obj1 is reference that reffers to object of class Demo
    obj2 = Demo()

    obj1.fun()#fun(obj1)
    obj2.fun()

    del obj1
    del obj2


if __name__ == '__main__':
    main()
