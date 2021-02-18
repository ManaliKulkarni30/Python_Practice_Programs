#1 : Function accepts nothing and return nothing
def fun():
    print("Function fun")

#2 : Function which accepts parameter and return nothing
def gun(no):
    print("Function gun with parameter",no)

#3 : Function which accepts parameter and return value
def sun(no):
    print("Function sun with parameter",no)
    return no+1

#4 : Functions acepts multiple values and return multiple values
def addSub(no1,no2):
    print("Function addSub with multiple parameter")
    add = no1 + no2
    sub = no1 - no2
    return add,sub

#5 : Nested Functions
def Mervellous():
    print("Inside Marvellous")
    def Infosystems():
        print("Inside Infosystems")
    Infosystems()#we can't call this function ouside the scope of outer Function

#6 :only Delcaring Function we can use pass(13 Feb 2021)
def mun():
    pass

#main function
def main():
    fun()
    gun(11)
    ret = sun(21)
    print("Return value for sun is ",ret)

    ret1,ret2 = addSub(101,51)
    print("Addition is :",ret1)
    print("Subtraction is:",ret2)

    Mervellous()

    mun()

if __name__ == "__main__":
    main()
