class student():
    def __init__(self,name,rollno,javamarks,pythonmarks,mathsmarks):
        self.name = name
        self.rollno = rollno
        self.javamarks = javamarks
        self.pythonmarks = pythonmarks
        self.mathsmarks = mathsmarks
    def printalldetails(self):
        print(self.name)
        print(self.rollno)
        print(self.javamarks)
        print(self.pythonmarks)
        print(self.mathsmarks)
obj1 = student('sahithi',116,82,89,98)
obj1.printalldetails()
obj2 = student('harsha',109,88,82,86)
obj2.printalldetails()
obj3 = student('saranya',110,76,87,98)
obj3.printalldetails()
