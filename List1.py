def DisplayL(list):
    iCnt = 0
    for iCnt in range(len(list)):
        print(list[iCnt])

def main():
    arr = [10,20,30,40,50]
    print(arr)
    print(arr[3])

    #we can store heterogenous data in list
    Brr =[10,"Manali",66.48,"Pune"]
    print(Brr)

    DisplayL(arr)

if __name__ == "__main__":
    main()
