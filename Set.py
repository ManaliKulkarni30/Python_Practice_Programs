def main():
    arr = {10,20,30.5,"Hello"}

    print(type(arr))
    print(arr)

    print(len(arr))

    for value in arr:
        print(value)

    arr.add(20.3)
    print(arr)

    arr.remove(20.3)
    print(arr)

    arr.discard(30.5)
    print(arr)

    arr.pop()#Don't use on set since the result is unpredictable
    print(arr)

if __name__ == '__main__':
    main()
