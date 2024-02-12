# object oriented programming.
class Persons:  # class is a blueprint of something
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

person1 = Persons("Drew", 4, "riding")
person2 = Persons("Eman", 20, "hiking")

print("Hi, my name is", person1.name)