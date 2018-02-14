import random


class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name 
    
    def alive(self):
            return self.health > 0


    def print_status(self):
        print("{} has {} health and {} power".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)
      
    def attack(self, enemy):
        raw_input == input()
        if raw_input == "1":
            enemy.health -= self.power
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
            if enemy.health <= 0:
                print("The {} is dead.".formant(enemy.name))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            
        else:
            print("Invalid input {}".format(raw_input))


class Goblin(Character):
    def __init__(self, health, power, name):
       super().__init__(health, power, name)
    def attack(self, hero):
         if goblin.health > 0:
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

class Zombie(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)
    def attack(self, hero):
            if hero.health > 0:
               hero.health -= zombie.power
               print("The zombie does {} damage to you".format(zombie.power))
               if hero.health <= 0:
                   print("Braaaiinss")
    def revive(self, enemy):
            if self.health <= 0:
                self.health += 100
                print("{} walks no more".format(enemy.name))



class Medic(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)
    def attack(self, hero):
        if hero.health > 0:
            hero.health -= medic.power
            print("The medic does {} damage to you".format(medic.power))
            if hero.health <= 0:
                print("Better luck next time!")
    def heal(self, enemy):
        if self.health < 15:
            chance = random.randint(0, 100)
            if chance <= 20:
                self.health += 2
                print("{} has healed for 2 points!".format(enemy.name))

class Shadow(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)
        

def main():
    hero = Hero (10, 6, 'Strongguy')
    goblin = Goblin (10, 2, 'Greenboy')
    zombie = Zombie (50, 50, 'Brainboy')
    medic = Medic (15, 3, 'HealMcGeal')
    
   
    enemy = []
    menuchoice = input("Which enemy would you like to fight? Press 1 or 2: \n1 goblin, \n2. zombie, \n3. medic \n: " )

    if menuchoice == "1":
        enemy = goblin

    if menuchoice == "2":
        enemy = zombie
    
    if menuchoice == "3":
        enemy = medic

    while enemy.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The {} has {} health and {} power.".format(enemy.name, enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. Fight", enemy.name)
        print("2. Do nothing")
        print("3. Flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            if random.randint(0, 100) <= 20:
                enemy.health -= hero.power * 2
                print("You do {} damage to the {}.".format(hero.power, enemy.name))
            else:
                enemy.health -= hero.power
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
            medic.heal(enemy)
            if enemy.health <= 0:
                zombie.revive(enemy)

                print("The enemy is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            # Goblin attacks hero
            hero.health -= enemy.power
            print("The {} does {} damage to you.".format(enemy.name, enemy.power))
            if hero.health <= 0:
                print("You are dead.")

main()
