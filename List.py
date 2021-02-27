def Addition(list):
    iCnt = 0
    iSum = 0
    for iCnt in range(len(list)):
        iSum = iSum + list[iCnt]
    return iSum

def main():
    size = int(input("Enter the number of elements:"))

    arr = []
    print("Enter the elements:")
    for i in range(size):
        print("Enter the number :",i+1)
        value = int(input())
        arr.append(value)

    print("Accepted data is:",arr)

    ans = Addition(arr)
    print("Addition of numbers in arr is:",ans)

if __name__ == "__main__":
    main()
