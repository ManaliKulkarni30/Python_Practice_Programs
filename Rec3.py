i = 0

def fun():
    global i
    print(i)
    i = i+1
    fun()

def main():
    fun()

if __name__ == '__main__':
    main()
