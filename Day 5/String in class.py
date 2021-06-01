class Myclass:

    def func1(self):
        print("HELLO")

    def func2(self,name):
        self.name = name

    def func3(self):
        print("Value is:",self.name)

h1 = Myclass()
h1.func1()
h1.func2('Devalsinh')
h1.func3()
