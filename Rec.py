#Demonstration of Recursion
#Recursion means calling function from same function itself

#Display Iterative
def DisplayI(no):
    for i in range(no):#Iteration
        print("Hello")

#Display Rcursive
def DisplayR(no):
    if no != 0:
        no = no -1
        print("Hello")
        DisplayR(no)#Recursive call

def main():
    print("Enter number of iterations:")
    no = int(input())

    print("Calling Iterative function")
    DisplayI(no)

    print("Calling Recursive function")
    DisplayR(no)

if __name__ == '__main__':
    main()
