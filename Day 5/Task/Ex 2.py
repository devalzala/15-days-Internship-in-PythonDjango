class Cal2:
    radius=0
    def setdata(self):
        r = int(input("Enter radius: "))
        self.radius=r
    
    def display(self):
        area = 3.14*self.radius * self.radius
        print("sum is ",area)

c = Cal2()
c.setdata()
c.display()