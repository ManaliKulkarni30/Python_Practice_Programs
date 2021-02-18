import sys

def add(no1,no2):
    return no1+no2

def main():
    #validation
    if((len(sys.argv)<3) or (len(sys.argv) > 3)):
        print("invalid number of arguments")
        return

    ret = add(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is:",ret)

if __name__ == "__main__":
    main()
