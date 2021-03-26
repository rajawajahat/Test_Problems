class Dog():
    pass

    def bark(self):
        print("Dog started barking")
        
class Cat():
    pass

    def meow(self):
        print("Cat started meowing")


def pet_calling(pet):
    
    if isinstance(pet, Dog):
        pet.bark()
    elif isinstance(pet, Cat):
        pet.meow()
    else:
        raise Exception("Sorry, Wrong Object")

if __name__ == '__main__':
    my_object = Cat()
    pet_calling(my_object)