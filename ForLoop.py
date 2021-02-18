def DisplayF(val):
    iCnt = 0
    for iCnt in range(0,val):
        print("Jay Ganesh")

def DispalyW(val):
    iCnt = 0
    while iCnt < val:
        print("Jay Ganesh")
        iCnt = iCnt + 1

def main():
    print("Enter the number of iterations:")
    no = int(input())
    print("Output of For Loop")
    DisplayF(no)
    print("Output of while loop")
    DispalyW(no)
if __name__ == "__main__":
    main()
