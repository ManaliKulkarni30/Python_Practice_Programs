# Write a program to accept n elements from user and check whether numbers are even , odd or perfect using oop

class Number:
    def __init__(self, no = 10):
        self.size = no
        self.arr = []

    def __del__(self):
        print("Inside Destructor")
        del self.arr

    def Accept(self):
        print("Enter the elements:")
        for i  in range(self.size):
            self.arr.append(int(input()))

    def Display(self):
        print("Elemments in list are:")
        for i in range(self.size):
            print(self.arr[i],end=" ")

    def Sum(self):
        sum = 0
        for i in range(self.size):
            sum = sum + self.arr[i]
        return sum

    def chkEven(self):
        for i in range(self.size):
            if self.arr[i] % 2 == 0:
                print(self.arr[i],end=" ")
        print("\r")

    def chkPerfect(self):
        for i in range(self.size):
            sum = 0
            for j in range(1,int(self.arr[i]/2)+1):
                if self.arr[i] % j == 0:
                    sum = sum + j
            if sum == self.arr[i]:
                print(self.arr[i],end=" ")
        print("\r")


def main():
    no = int(input("Enter how many numbers do you want:"))

    obj1 = Number(no)

    obj1.Accept()
    obj1.Display()

    ret = obj1.Sum()
    print("Sum of all elements of list is:",ret)

    print("Display even number in list:")
    obj1.chkEven()

    print("Display perfect number in list:")
    obj1.chkPerfect()

    del obj1


if __name__ == '__main__':
    main()
