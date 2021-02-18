#13 Feb 2021
#1 : Positional Argument
def student(name,rno,address,marks):
    print("Name of student:",name)
    print("Name of rno:",rno)
    print("Name of address:",address)
    print("Name of marks:",marks)

#2 : Keyword Argument
def computer(RAM,Processor,HDD):
    print("RAM Size is:",RAM)
    print("Processor is:",Processor)
    print("Size of HDD is:",HDD)

#3 : Default argument(It's sequence should be right to left not left to right)
def circleArea(radius,PI=3.14):
    print("Value of PI is:",PI)
    return radius*radius*PI
#4 : Variable number of arguments
def fun(*values):
    print("Number of arguments:",len(values))

def main():
    student("Manali",11,"pune",56)#positional argument

    computer(HDD="1TB",RAM=8,Processor="i5")#keyword argument defining argument name and value simultaneously

    circleArea(10.25)#defult argument
    circleArea(10.25,7.12)#Default Argument

    fun(10)
    fun(10,20,30,40,50)
    
if __name__ == "__main__":
    main()
