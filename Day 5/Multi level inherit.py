class Parent:

    def __init__(self):
        print('Calling Parent Constuctor')

    def parentmethod(self):
        print('Calling Parent Method')

class Child(Parent):

    def __init__(self):
        print('Calling Child Constuctor')

    def childmethod(self):
        print('Calling Child Method')

    def __init__(self):
        print('Calling Child Constuctor')

    def childmethod(self):
        print('Calling Child Method')

class Subchild(Child):

    def __init__(self):
        print('Calling Subchild Constuctor')

    def subchildmethod(self):
        print('Calling Subchild Method')

sc = Subchild()
sc.subchildmethod()
sc.childmethod()
sc.parentmethod()
