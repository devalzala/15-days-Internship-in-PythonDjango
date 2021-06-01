class Publisher:
    name = "World Publication"
    def display(self):
        print("Name: ",self.name)

class Book(Publisher):
    pageNo = "1050"
    def display1(self):
        print("pageNo: ",self.pageNo)

class Tape(Publisher):
    time = 100
    def display2(self):
        print("Time: ",self.time)

b = Book()
t = Tape()
b.display()
b.display1()
t.display2()