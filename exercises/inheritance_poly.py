class Animal():
    def __init__(self, species, gender):
        self.species = species
        self.species = gender
        print ("ANIMAL CREATED")

    def action(self, choice):
        if choice == 1:
            print ('purrs')
        elif choice == 2:
            print ('eats')
        elif choice == 3:
            print ('sleep')

    def who_am_i(self):
        print ("I am an animal")


animal1 = Animal("tiger", "male")

print (animal1)

print (animal1.action(2))


# passing animal class into dog class will make methods belonging to animal available to dog
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
        print ("DOG CREATED")

    def who_am_i(self):
        print ("I am a dog")

    def bark(self):
        print ("BARK")


dog1 = Dog("dobber", 'female', 'lucky')


print (dog1)

print (dog1.bark())
