import os
import threading
from time import sleep

def Thread1(no):
    print("Thread1")
    print("PID of Thread1:",os.getpid())
    for i in range(no):
        sleep(1)
        print("Thread1 :",i)


def Thread2(no):
    print("Thread2")
    print("PID of Thread2:",os.getpid())
    for i in range(no):
        sleep(1)
        print("Thread2 :",i)

def main():
    print("Inside main")
    print("PID of main process:",os.getpid())
    print("PID of parent process of main:",os.getppid())

    value = 10

    p1 = threading.Thread(target=Thread1,args=(value,))
    p2 = threading.Thread(target=Thread2,args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == '__main__':
    main()
