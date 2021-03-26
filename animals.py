class Animal:
    def __init__(self, name):
        self.name = name
        
    def whoami(self):
        return self.name
    
    def speak(self):
        return "The animal refuses to speak"
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        return "Meow!"
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        return "Woof!"
    
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        
if __name__ == '__main__':
    
    animals = [Dog("Rover"), Cat("Hank"), Fish("Fred")]

    for animal in animals:
        print("This animal's name is {}".format(animal.name))
        print(animal.speak())