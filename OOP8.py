class Student:
    school = "Abhinav" #Class Variable

    def __init__(self,no1,no2,no3):
        self.m1 = no1   #Instance Variable
        self.m2 = no2
        self.m3 = no3

    def instance_Total(self):            #Instance Method
        print("Inside instance method")
        return self.m1+self.m2+self.m3

    @classmethod   #decorator
    def class_DisplaySchool(cls):        #Class Method
        print("School Name is:",cls.school)

    @staticmethod    #decorator
    def static_Info():      #static Method
        print("This class contains information of school")

def main():

    Student.static_Info() #Calling Static method
    Student.class_DisplaySchool() #calling class Method

    obj1 = Student(80,50,70)
    obj2 = Student(65,80,75)

    ret = obj1.instance_Total()
    print("Total marks of student 1 is:",ret)
    ret = obj2.instance_Total()
    print("Total marks of student 2 is:",ret)

if __name__ == '__main__':
    main()
