import os
import time

def Square(no):
    return no*no

def SerialProcessing():
    start = time.time()
    ret = []
    arr = range(10)

    for i in arr:
        ret.append(Square(arr[i]))

    end = time.time()
    print("Processing time:",end-start)
    #print(ret)

def main():

     SerialProcessing()

if __name__ == '__main__':
    main()
