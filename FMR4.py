#Filter Map Reduce 4
#Accept n numbers from user, filter even no's and add 2 in each of them and calculate sum of all these no's
import  functools as ft

def main():
    size = int(input("Enter the number of elements:"))
    arr = []

    print("Enter the elements:")
    for i in range(size):
        print("Enter the number :",i+1)
        value = int(input())
        arr.append(value)

    print("Accepted data is:",arr)

    newData = list(filter(lambda no:(no % 2 == 0),arr))
    print("Data After Filteration:",newData)#printing new recived array of even elements

    newData1 = list(map(lambda no: no+2,newData))
    print("Data After Mapping:",newData1)

    output = ft.reduce(lambda no1,no2:no1+no2,newData1)
    print("Data After Reduce:",output)



if __name__ == '__main__':
    main()
