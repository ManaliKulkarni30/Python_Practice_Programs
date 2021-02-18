def StartDynamic(No,message = "Jay Ganesh"):
    iCnt = 0
    while iCnt < No:
        print(message)
        iCnt = iCnt + 1

def main():
    print("How many times do you want output:")
    no = int(input())
    print("Enter a message you want to print:")
    msg = input()
    StartDynamic(no,msg)
    StartDynamic(no)

if __name__ == "__main__":
    main()
