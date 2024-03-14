class Tiger:
    def init(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def roar(self):
        print(f"{self.name} roars ferociously!!")

    def attack(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f"{self.name} pounces on {opponent.name} and deals {damage} damage.")

class Lion:
    def init(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15

    def roar(self):
        print(f"{self.name} roars loudly!")

    def attack(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} with its sharp claws and deals {damage} damage.")

# Creating instances of Tiger and Lion
tiger = Tiger("Bengal Tiger")
lion = Lion("African Lion")

# Game loop
rounds = 1
while tiger.health > 0 and lion.health > 0:
    print(f"\nRound {rounds}")
    tiger.roar()
    tiger.attack(lion)
    if lion.health <= 0:
        print(f"\nThe {lion.name} is defeated! The {tiger.name} wins!")
        break

    lion.roar()
    lion.attack(tiger)
    if tiger.health <= 0:
        print(f"\nThe {tiger.name} is defeated! The {lion.name} wins!")
        break

    rounds += 1