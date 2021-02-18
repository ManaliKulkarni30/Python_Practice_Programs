#Definition of addtion function
def addition(val1,val2):
    ret = val1 + val2
    return ret

#Definition of addtion function
def subtraction(val1,val2):
    ret = val1 - val2
    return ret

#Flow of program
#Start 23 24 12 -> 16 2 16 17 7 17 19 20 End

#Entry point function
def main():
    no1 = int(input("Enter number one:"))
    no2 = int(input("Enter number two:"))

    ans1 = addition(no1,no2)
    ans2 = subtraction(no1,no2)

    print("Addition is:",ans1)
    print("Subtraction is:",ans2)

#code starter
if __name__ == "__main__":
    main()
