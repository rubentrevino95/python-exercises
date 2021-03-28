class Character:
  
    isElf = False

    inv = []

    def __init__(self, name, job, health):
        self.name = name
        self.job = job
        self.health = health

    def description(self):
        return "{} is a {}".format(self.name, self.job)

    def speak(self):
        return "{} says hello".format(self.name)

    def attack(self):
         hit = range(-1,-10)
         return  health - hit
 


c1 = Character('Anon1', 'DPS', 100)
c2 = Character('Anon2', 'Tank', 100)
c3 = Character('Anon3', 'Healer', 100)

print(c1.description())
print(c1.speak())