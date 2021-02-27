#Filter Map Reduce 3
#Accept n numbers from user, filter even no's and add 2 in each of them and calculate sum of all these no's
import  functools as ft

chkEven = lambda no:(no % 2 == 0)
increment = lambda no: no+2
Add = lambda no1,no2:no1+no2

def main():
    size = int(input("Enter the number of elements:"))
    arr = []

    print("Enter the elements:")
    for i in range(size):
        print("Enter the number :",i+1)
        value = int(input())
        arr.append(value)

    print("Accepted data is:",arr)

    newData = list(filter(chkEven,arr))
    print("Data After Filteration:",newData)#printing new recived array of even elements

    newData1 = list(map(increment,newData))
    print("Data After Mapping:",newData1)

    output = ft.reduce(Add,newData1)
    print("Data After Reduce:",output)



if __name__ == '__main__':
    main()
