#Inbuilt Function Model
def Subtraction(no1,no2):
    print("3:Inside Subtraction")
    return no1-no2

def SubDecorator(func_name):
    print("7: Inside SubDecorator")
    def Updator(a,b):
        print("9:Inside Updator")
        if a < b:
            temp = a
            a = b
            b = temp
        return func_name(a,b)
    return Updator

def main():

    print("19:Inside main")
    sub = SubDecorator(Subtraction)

    no1 = int(input("Enter first number:"))
    no2 = int(input("Enter second number:"))

    ret = sub(no1,no2)

    print("Subtraction is:",ret)
    print("28:End of main")


if __name__ == '__main__':
    print("32:Inside starter")
    main()
