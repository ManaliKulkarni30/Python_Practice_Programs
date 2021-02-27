#Highet number of recursive stackframe
import sys

def main():
    print("Get Recursion limit:",sys.getrecursionlimit())

    sys.setrecursionlimit(1500)

    print("New Recursion Limit:",sys.getrecursionlimit())

if __name__ == '__main__':
    main()
