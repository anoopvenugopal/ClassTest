class StudentRec:
    __rollNo=0
    __name=""
    __add=""
    __phone=""
    def addData(self):
        self.__rollNo=int(input("Enter RollNo:\t"))
        self.__name = input("Enter Name:\t")
        self.__add = input("Enter address:\t")
        self.__phone = input("Enter phone:\t")
    def showData(self):
        print("RollNo\t:",self.__rollNo)
        print("Name\t:", self.__name)
        print("add\t:", self.__add)
        print("Phone\t:", self.__phone)


def main():
    s1=StudentRec()
    s1.addData()
    s1.showData()

if __name__=="__main__":
    main()
