class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(self.name,"is barking!")


dog1 = Dog("Alfa", 3, "czarny")
dog1.sound()

dog2 = Dog("Beta", 1, "biały")
dog2.sound()

dog3 = Dog("Gamma", 2, "brązowy")
dog3.sound()
