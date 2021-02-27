#name = lambda parameter: body
sum = lambda no1,no2:no1+no2#We can consider sum name  as function pointer in C, Sum is name of reference to the lambda function

def fun(name):
    ret = name(10,20)
    print("Value in fun is:",ret)

#named function
def Addition(no1,no2):
    return no1+no2

def main():
    val1 = int(input("Enter first number:"))
    val2 = int(input("Enter Second number:"))
    ret = Addition(val1,val2)
    print("Addition is:",ret)
    ret = sum(val1,val2)
    print("Addition with lambda is:",ret)
    fun(sum)
    
if __name__ == "__main__":
    main()
