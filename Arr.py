from array import *

def main():
    arr = array('i',[11,21,51,101,111])
    print(type(arr))
    print(len(arr))
    print(arr)
    for i in range(len(arr)):
        print(arr[i],end="")
    print("\r")

    for no in arr:
        print(no,end="")
    print("\r")

    icnt = 0
    while icnt < len(arr):
        print(arr[icnt])
        icnt+=1
    print("\r")



if __name__ == '__main__':
    main()
