def main():
    batches = {"PPA":12500, "LB":11000, "Python":13000, "Angular" : 10000}
    batches["LSP"] = 11000

    print("Keys of dictionary")
    for value in batches.keys():
        print(value)

    print("Keys and values of dictionary")
    for value in batches.keys():
        print(value, batches[value])

    print("keys and values are")
    for i,j in batches.items():
        print(i,j)

if __name__ == "__main__":
    main()
