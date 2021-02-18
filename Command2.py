import sys

def add(no1,no2):
    return no1+no2

def main():
    ret = add(int(sys.argv[1]),int(sys.argv[2]))
    print("Addition is:",ret)

if __name__ == "__main__":
    main()
