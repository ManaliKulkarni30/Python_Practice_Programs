
class Arithematic:
    #class Defination
    value = 111#instance variable
    def __init__(self,i,j):#Constructors (instance method), self is similar to this pointer
        self.no1 = i #class instance variable
        self.no2 = j #Class instance variable
        print("Inside constructor")

    def Add(self):#Instance method
        print(self.value)
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2

def main():
    obj1 = Arithematic(21,11)#__init__(obj1,21,11)
    obj2 = Arithematic(101,51)#__init__(obj2,101,51)

    
    print(obj2.value)

    ret = obj1.Add()
    print("Addition is:",ret)
    ret = obj1.Sub()
    print("Substraction is:",ret)

    ret = obj2.Add()
    print("Addition is:",ret)
    ret = obj2.Sub()
    print("Substraction is:",ret)


if __name__ == '__main__':
    main()
