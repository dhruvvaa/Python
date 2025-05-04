class person:
    def data(self,name,age):
        self.name=name
        self.age=age
    def call(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old.")
person1=person()
person1.data("Dhruva",19)
person1.call()