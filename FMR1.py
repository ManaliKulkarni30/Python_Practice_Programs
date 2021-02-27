#Functional Programming
#Filter Map Reduce 1
#Accept n numbers from user, filter even no's and add 2 in each of them and calculate sum of all these no's
def chkEven(no):#Function of checking even values
    if no%2 == 0:
        return True
    else:
        return False

def MarvellousFilter(arr):#Function to filter even data
    brr = []
    for i in range(len(arr)):
        if chkEven(arr[i]) == True:
            brr.append(arr[i])
    return brr

def MarvellousMap(arr):#Function to add 2 in each even number
    for i in range(len(arr)):
        arr[i] = arr[i] + 2
    return arr

def MarvellousReduce(arr):#function add all even numbers
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum


def main():
    size = int(input("Enter the number of elements:"))
    arr = []

    print("Enter the elements:")
    for i in range(size):
        print("Enter the number :",i+1)
        value = int(input())
        arr.append(value)

    print("Accepted data is:",arr)

    newData = MarvellousFilter(arr)
    print("Data After Filteration:",newData)#printing new recived array of even elements

    newData1 = MarvellousMap(newData)
    print("After Map New Data is:",newData1)

    ret = MarvellousReduce(newData1)
    print("After reduce function:",ret)

if __name__ == '__main__':
    main()
