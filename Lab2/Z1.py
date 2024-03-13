class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        print()


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print(self.name, "does woof woof")


class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print(self.name, "does meow meow")


class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        print(self.name, "does Squik")


fox = Fox("filemon", 2, "m")
fox.sound()
