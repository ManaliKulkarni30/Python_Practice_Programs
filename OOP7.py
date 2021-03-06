
class Marvellous:
    value1 = 11
    def __init__(self,no1,no2):
        print("Inside constructor")
        self.i = no1
        self.j = no2

    def __del__(self):
        print("Inside destructor")

    def fun(self):
        print("Inside fun method")
        print("Value of j is :",self.j)

def main():
    obj1 = Marvellous(11,21)
    obj2 = Marvellous(51,101)

    print("Value of i from obj1:",obj1.i)
    print("Value of i from obj2:",obj2.i)
    print("Value of class Marvellous:",Marvellous.value1)

    obj1.fun()
    obj2.fun()

    del obj1
    del obj2

if __name__ == '__main__':
    main()
