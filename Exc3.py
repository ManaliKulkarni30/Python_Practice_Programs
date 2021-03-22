class AgeInvalid(Exception):
    def __init__(self,data):
        self.data = data

def main():

    try:
        age = int(input("Enter a age:"))
        if age < 18:
            raise AgeInvalid("Your age is less than 18")
    except AgeInvalid as eobj:
        print("Exception occurs:",eobj)
    else:
        print("You'll get PAN Card within 7 working days")

if __name__ == '__main__':
    main()
