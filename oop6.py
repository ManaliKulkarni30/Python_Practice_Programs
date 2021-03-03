#Accept n numbers from users display even numbrs ,odd numbers, perfect numbers

class Demo:
    brr = []
    def __init__(self,n,arr):
        self.no = n
        for i in range(self.no):
            self.brr.append(arr[i])

    def chkEven(self):
        for i in range(self.no):
            if self.brr[i] % 2 == 0:
                print(self.brr[i],end=" ")
        print("\r")

    def chkOdd(self):
        for i in range(self.no):
            if self.brr[i] % 2 != 0:
                print(self.brr[i],end=" ")
        print("\r")

    def chkPerfect(self):
        for i in range(self.no):
            sum = 0
            iNo = self.brr[i]
            for j in range(2,self.brr[i]):
                if self.brr[i] % j == 0:
                    sum = sum + j
            if sum == self.brr[i]:
                print(self.brr[i],end=" ")
        print("\r")

def main():
    arr = []
    no = int(input("Enter how many numbers do you want:"))
    for i  in range(no):
        arr.append(int(input()))

    obj1 = Demo(no,arr)


    
    obj1.chkEven()
    obj1.chkOdd()
    obj1.chkPerfect()

if __name__ == '__main__':
    main()
