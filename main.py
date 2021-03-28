import time
import random

class Player():

  def __init__(self):
    self.hunger = 20
    self.health = 20
    self.gapples = 3
    self.accuracy = random.randint(1, 3)
    self.distance = 0
    self.arrows = 15
    self.steak = 10
    self.hungerlow = False
    self.healthlow = False
  
  def run(self, enemy):
    runamount = random.randint(1, 5)
    self.distance += runamount
    self.hunger -= round(runamount / 2)
    enemyrun = random.randint(1, 5)
    enemy.distance += enemyrun
    enemy.hunger -= round(enemyrun / 2)

  def heal(self, enemy):
    if self.gapples > 0:
      if 20 - self.health >= 8 and 20 - self.hunger >= 4:
        self.health += 8
        self.hunger += 4
        enemyrun = random.randint(1, 5)
        enemy.distance += enemyrun
        enemy.hunger -= round(enemyrun / 2)
        text = "You ate 1 Golden Appple"
        self.gapples -= 1
        return text
      self.health += 20 - self.health
      self.hunger += 20 - self.hunger
      enemyrun = random.randint(1, 5)
      enemy.distance += enemyrun
      enemy.hunger -= round(enemyrun / 2)
      text = "You ate 1 Golden Appple"
      self.gapples -= 1
      return text

    else:
      text = "You don't have any more Golden Apples."
      return text

  def eat(self, enemy):
    if self.steak > 0:
      if 20 - self.hunger >= 8:
        self.hunger += 8
        enemyrun = random.randint(1, 5)
        enemy.distance += enemyrun
        enemy.hunger -= round(enemyrun / 2)
        text = "You ate a steak"
        self.steak -= 1
        return text
      else:
        self.hunger += 20 - self.hunger
        enemyrun = random.randint(1, 5)
        enemy.distance += enemyrun
        enemy.hunger -= round(enemyrun / 2)
        text = "You ate a steak"
        self.steak -= 1
        return text
    else:
      text = "You don't have any more steak."
      return text
  
  def bowspam(self, target):
    if self.arrows > 0:
      shotslanded = self.accuracy
      if shotslanded > self.arrows:
        shotslanded = self.arrows
      self.arrows -= shotslanded
      damage = shotslanded
      target.health -= damage

      if shotslanded <= 5:
        run = random.randint(1, shotslanded)
        target.distance += run
        target.hunger -= round(run / 1)
      else:
        run = random.randint(1, shotslanded)
        target.distance -= run
        target.hunger -= round(run / 2)
      print(f"You landed {shotslanded} shots.  You did {damage} damage to the opponent.")
      if self.accuracy == 10:
        pass
      else:
        accuracyuplimit = random.randint(1, 10 - self.accuracy)
        self.accuracy += accuracyuplimit
        print(f"You accuracy has increased by {accuracyuplimit}")
    else:
      print("You don't have any more arrows to shoot.")

  def fight(self, target):
    self.health -= random.randint(1, self.health)
    target.health -= random.randint(1, target.health)
    enemyrun = random.randint(3, 10)
    selfrun = random.randint(1, 3)
    self.distance += selfrun
    target.distance += enemyrun
    self.hunger -= round(selfrun / 2)
    target.hunger -= round(enemyrun / 2)

  def stats(self):
    print("Actions:\n------------------\nRun: You will run away from your enemy a random amount\nof blocks, which depletes your hunger.\n\nHeal: Eats a Golden Apple if you have one, which heals 8 healthpoints and 4 hunger points.  Your enemy will keep moving behind you.\n\nEat:  Eats a steak which replenishes 8 hunger.\nYour enemy will keep moving while you are eating.\n\nBow Spam:  Shoot the enemy using arrows, damaging them \nand pushing them back based on your accuracy.\n\nFight:  Go into combat with your enemy,\nlosing random amounts of health\nand running a random amount.\n\nStats:  Check your stats and display the different\nactions and what they do.")
    print(
      f"Health:  {self.health}/20\nHunger:  {self.hunger}/20\nGolden Apples:  {self.gapples}\nArrows:  {self.arrows}\nAccuracy:  {self.accuracy}/10\nDistance: {self.distance}"
      )
  def check(self, target):
    if self.health <= 0:
      return "health"
    if self.health < 10:
      print("Uh Oh...  Your health is getting low.  You should heal if you still have Golden Apples...")
    if self.hunger <= 6:
      return "hunger"
    if self.hunger < 10:
      print("You are running low on hunger.  Time to eat?")
    if self.distance - target.distance <= 3:
      return "distance"
    if (self.distance - target.distance) <= 5:
      print("Run!  The enemy is closing in!")
  def compcheck(self):
    if self.health <= 0:
      return "health"
    if self.health < 10:
      self.healthlow = True
    if self.hunger <= 6:
      return "hunger"
    if self.hunger < 10:
      self.hungerlow = True



print("Hello!  Welcome to Jake's Adventure Game.")
print("To win, you must get 50 blocks away from your enemy, or you must defeat your enemy.")
print("You have 6 actions you can take along the way.\n------------------\nRun: You will run away from your enemy a random amount\nof blocks, which depletes your hunger.\n\nHeal: Eats a Golden Apple if you have one, which heals 8 healthpoints and 4 hunger points.  Your enemy will keep moving behind you.\n\nEat:  Eats a steak which replenishes 8 hunger.\nYour enemy will keep moving while you are eating.\n\nBow Spam:  Shoot the enemy using arrows, damaging them \nand pushing them back based on your accuracy.\n\nFight:  Go into combat with your enemy,\nlosing random amounts of health\nand running a random amount.\n\nStats:  Check your stats and display the different\nactions and what they do.")

game = True
while game:
  player = Player()
  player.distance = 5
  comp = Player()
  gametime = True
  while gametime:
    true = True
    #Get Input
    while true == True:
      try:
        choice = input("What action would you like to take?\n1. Run\n2. Heal\n3. Eat\n4. Bow Spam\n5. Fight\n6. Stats\n:   ")
        choices = ["1", "2", "3", "4", "5", "6"]
        yes = False
        for i in choices:
          if i == choice:
            yes = True
        if yes == False:
          print("That is not a valid action.")
        else:
          true = False
      except:
        print("That is not a valid action.")
    #End of get input
    if choice == "1":
      player.run(comp)
    elif choice == "2":
      text = player.heal(comp)
      print(text)
    elif choice == "3":
      text = player.eat(comp)
      print(text)
    elif choice == "4":
      player.bowspam(comp)
    elif choice == "5":
      player.fight(comp)
    elif choice == "6":
      player.stats()
    check = player.check(comp)
    if check == "health":
      print("Oh No!  You ran out of health and died.")
      gametime = False
      continue
    elif check == "hunger":
      print("You ran out of hunger!  The enemy easily caught up to\nyou and killed you.")
      gametime = False
      continue
    elif check == "distance":
      print("The enemy has closed in.  You have died.")
      gametime = False
      continue

    compcheck = comp.compcheck()
    if comp.healthlow:
      comp.heal(player)
    if comp.hungerlow:
      comp.eat(player)
    if compcheck == "health":
      print("Wow!  You defeated your opponent.  You Win!")
      gametime = False
      continue
    if compcheck == "hunger":
      print("Your enemy ran out of hunger.  You Win!")
      gametime = False
      continue
    if player.distance - comp.distance >= 50:
      print("You successfully got away!  You Win!")
      gametime = False
      continue

  while True:
    try:
      again = input("Do you want to play again?:  ")
      if again != "yes" and again != "no":
        print("That is not a valid answer.")
      elif again == "yes":
        print("Ok!  Setting up a new game...")
        break
      elif again == "no":
        print("Thanks for Playing")
        game = False
        break
    except:
      print("That is not a valid answer.")