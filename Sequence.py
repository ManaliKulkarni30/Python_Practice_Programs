def main():
    arr = (11,21,23.5,"Hello")

    print(type(arr))

    for i in range(len(arr)):
        print(arr[i])

    arr[0] = 12

    print(arr[0])

if __name__ == '__main__':
    main()
