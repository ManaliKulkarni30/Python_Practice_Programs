#Addition of two numbers
#Date: 06 feb 2021

#type 1 Using hardcoded values
"""
no1 = 11
no2 = 21
ans = no1 + no2
print("Addition is:",ans)
"""

#Type 2 Accepting i/p from user
"""print("Enter number one:")
no1 = input()
print("Enter number two:")
no2 = input()
ans = no1 + no2
print("Addition is:",ans)
"""

#Type 3 typecasting after taking i/p
"""
print("Enter number one:")
no1 = input()
print("Enter number two:")
no2 = input()
ans = int(no1) + int(no2)#typecasting or type conversion
print("Addition is:",ans)
"""

#Type 4 typecasting while taking i/p
"""
print("Enter number one:")
no1 = int(input())
print("Enter number two:")
no2 = int(input())
ans = no1 + no2
print("Addition is:",ans)
"""

#Type 5 using in function alert of input function
"""
no1 = int(input("Enter number one:"))
no2 = int(input("Enter number two:"))
ans = no1 + no2
print("Addition is:",ans)
"""
#Type 6 Using function
#Because of writing function the code is become reusable
"""
def addition(val1,val2):
    ret = val1 + val2
    return ret

def main():
    no1 = int(input("Enter number one:"))
    no2 = int(input("Enter number two:"))
    ans = addition(no1,no2)
    print("Addition is:",ans)
#print(__name__)

if __name__ == "__main__":
    main()
"""
#Type 7
"""
import Mrvellous
def main():
    no1 = int(input("Enter number one:"))
    no2 = int(input("Enter number two:"))
    ans = Mrvellous.addition(no1,no2)
    print("Addition is:",ans)
#print(__name__)

if __name__ == "__main__":
    main()
"""

#Type8
def Addition(no1,no2):
    ans = no1 + no2
    return ans

def main():
    print("Enter firt number:")
    val1 = int(input())
    print("Enter Second number:")
    val2 = int(input())
    ret = Addition(val1,val2)
    print("Addition of {} and {} is: {}".format(val1,val2,ret))

if __name__ == "__main__":
    main()
