#Procedural Way

def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2

def main():
    value1 = int(input("Enter first number:"))
    value2 = int(input("Enter second number:"))

    ret = Add(value1,value2)
    print("Addition is:",ret)

    ret = Sub(value1,value2)
    print("Substraction is:",ret)

if __name__ == '__main__':
    main()
