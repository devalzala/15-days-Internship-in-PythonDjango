class hey:
    side, squareArea = 0,0 # side and area var
    def setdata(self):
        a = int(input("Enter side of square:"))
        self.side = a
    
    def area(self):
        self.squareArea = self.side*self.side

    def display(self):
        print("Area of square is= ",self.squareArea)

cal = hey()
cal.setdata()
cal.area()
cal.display()