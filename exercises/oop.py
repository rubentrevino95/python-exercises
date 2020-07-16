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
ruben = Person(name='Ruben', gender='male', age=24)

# print(type(ruben))

print (ruben.name, ruben.gender, ruben.age, ruben.species)

print (ruben.speak())

# methods are function in classes
