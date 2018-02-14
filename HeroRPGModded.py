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
            enemy_health -= self.power
            print("You do {} damage to the goblin.".format(hero_power))
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            
        else:
            print("Invalid input {}".format(raw_input))


class Goblin:
    def __init__(self, health, power, name):
       super().__init__(health, power, name)
    def attack(self, hero):
         if goblin_health > 0:
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")


    

    

def main():
    hero = Hero (10, 6, 'Strongguy')
    goblin = Goblin (10, 2, 'Greenboy')
    zombie = Zombie (50, 50, 'Brainboy')
   
    enemy = []
    menuchoice = input("Which enemy would you like to fight? Press 1 or 2: \n1 goblin, \n2. zombie" )

    if menuchoice == "1":
        enemy = goblin

    if menuchoice == "2":
        enemy = zombie

    while enemy.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
        print()
        print("What do you want to do?")
        print("1. fight", enemy.name)
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            if random.randint(0, 100) >= 20: 
                goblin_health -= hero_power * 2
                print("You do {} damage to the goblin.".format(hero_power))
            else:
                goblin_health -= hero_power
            print("You do {} damage to the goblin.".format(hero_power))
        if enemy.health <= 0:
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
            print("The enemy does {} damage to you.".format(enemy.power))
            if hero.health <= 0:
                print("You are dead.")

main()
