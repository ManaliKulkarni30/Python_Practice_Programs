def Addition(no1,no2):
    return no1+no2

def main():
    val1 = int(input("Enter first number:"))
    val2 = int(input("Enter Second number:"))
    ret = Addition(val1,val2)
    print("Addition is:",ret)    

if __name__ == "__main__":
    main()
