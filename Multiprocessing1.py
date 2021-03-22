import os
import multiprocessing

def Process1():
    print("Inside Process1")
    print("PID of process1:",os.getpid())
    print("PID of parent process of process1:",os.getppid())

def Process2():
    print("Inside Process2")
    print("PID of process2:",os.getpid())
    print("PID of parent process of process2:",os.getppid())

def main():
    print("Inside main")
    print("PID of main process:",os.getpid())
    print("PID of parent process of main:",os.getppid())

    p1 = multiprocessing.Process(target=Process1,args=())
    p2 = multiprocessing.Process(target=Process2,args=())

    p1.start()
    p2.start()

    print("End of main")

if __name__ == '__main__':
    main()
