class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    
    def introduce(self):
        print (f"Hello {self.name}. You are {self.age} years old and {self.gender} is my gender")
    
a = Person("Eniola", 12, "Male")
a.introduce()