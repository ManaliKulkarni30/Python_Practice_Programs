import os

def main():
    print("Inside main")

    print("PID of process:",os.getpid())

    print("PID of parent process:",os.getppid())

if __name__ == '__main__':
    main()
