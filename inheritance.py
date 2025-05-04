class animal:
    def speaks(self):
        print("Animal speaks")
class dog(animal):
    def barks(self):
        print("Dog barks")
dog1=dog()
dog1.speaks()
dog1.barks()