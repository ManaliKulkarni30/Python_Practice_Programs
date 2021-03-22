def main():
    arr = {10,20,30,40}

    print(type(arr))

    temp = list(arr)

    print(type(temp))

    temp[1] = 21

    arr = set(temp)

    print(arr)

if __name__ == '__main__':
    main()
