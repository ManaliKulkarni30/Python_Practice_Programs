def Addition(list):
    iCnt = 0
    iSum = 0
    for iCnt in range(len(list)):
        iSum = iSum + list[iCnt]
    return iSum

def main():
    arr = [10,20,30,40,50]
    ans = Addition(arr)
    print("Addition of numbers in arr is:",ans)

if __name__ == "__main__":
    main()
