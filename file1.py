def main():
    name = input("Enter the name of file:")

    fobj = open(name,"r")

    print(fobj.read())
    
if __name__ == '__main__':
    main()
