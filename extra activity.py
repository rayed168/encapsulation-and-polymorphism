class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("The animal's name is : ",self.name)
        print("The animal's age is : ",self.age)


class Own_Animal(Animal):
    def __init__(self, name, age, animal_type, breed):
        super().__init__(name, age)
        self.breed = breed
        self.animal_type = animal_type
    def info(self):
     super().info()
     print("The animal's type is : ",self.animal_type)
     print("The animal's breed is : ",self.breed)

name = input("Enter the name of your animal : ")
age = int(input("Enter the age of your animal : "))
animal_type = input("Enter the type of your animal : ")
breed = input("Enter the breed of your animal : ")

obj = Own_Animal(name, age, animal_type, breed)
obj.info()