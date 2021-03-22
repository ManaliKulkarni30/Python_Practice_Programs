def main():
    name = input("Enter the name of file:")

    fobj = open(name,"w")

    str = input("Enter the data you want to write in file")

    fobj.write(str)

if __name__ == '__main__':
    main()
