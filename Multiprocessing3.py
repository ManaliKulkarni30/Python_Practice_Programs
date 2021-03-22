import os
import multiprocessing

def Process1(no):
    print("Inside Process1")
    print("PID of process1:",os.getpid())
    print("PID of parent process of process1:",os.getppid())

    for i in range(no):
        print("Process1 :",i)


def Process2(no):
    print("Inside Process2")
    print("PID of process2:",os.getpid())
    print("PID of parent process of process2:",os.getppid())

    for i in range(no):
        print("Process2 :",i)

def main():
    print("Inside main")
    print("PID of main process:",os.getpid())
    print("PID of parent process of main:",os.getppid())

    value = 100

    p1 = multiprocessing.Process(target=Process1,args=(value,))
    p2 = multiprocessing.Process(target=Process2,args=(value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__ == '__main__':
    main()
