class Parent:


    def __init__(self):
        print('Calling parent constructor')
    
    def parentmethod(self):
        print('Calling parent method')

class Child(Parent):

    def __init__(self):
        print('Calling child constructor')

    def childmethod(self):
        print('Calling child method')

c = Child()
c.childmethod()
c.parentmethod()