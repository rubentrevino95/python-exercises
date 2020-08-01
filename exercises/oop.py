# class name
class Person():
    # class object attribute
    # same for any instance of a class
    species = 'human'

    # constructor
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # method
    def speak(self):
        print ("Hello! My name is {}".format(self.name))


# creating instance of object
person1 = Person(name='Ruben', gender='male', age=24)

# print(type(ruben))

print (person1.name, person1.gender, person1.age, person1.species)

print (person1.speak())

# methods are function in classes
