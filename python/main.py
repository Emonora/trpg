'''
Welcome to the TRPG source code, condensed into a single file for ease of use.

Author: August/Emonora

'''

import random, curses, time, math

stdscr = curses.initscr()
stepCounter = ["Right", 18]
questCounter = [False, 0]
pneumonoultramicroscopicsilicovolcanoconiosis: bool = False

# Classes
class Player:
    def __init__(self, health, resistance, defense, attack):
        self.health = health
        self.resistance = resistance
        self.defense = defense
        self.attack = attack
    def __str__(self):
        returned = f"Health: {self.health}, Resistance: {self.resistance}, Defense: {self.defense}, Attack: {self.attack}"
        return returned

class Enemy:
    def __init__(self, health, resistance, defense, attack):
        self.health = health
        self.resistance = resistance
        self.defense = defense
        self.attack = attack
    def __str__(self):
        returned = f"Health: {self.health}, Resistance: {self.resistance}, Defense: {self.defense}, Attack: {self.attack}"
        return returned

# Intro code
playerType: list[str] = ["Mage", "Knight", "Assassin"]
stdscr.addstr(4, 4, "Welcome to TRPG! A fully open source, souls-like text based rpg. ")
stdscr.refresh()
time.sleep(1)
stdscr.clear()
stdscr.addstr(4,4, "If you haven't already, please extend your output/terminal window to the maxium width, for best gameplay")
stdscr.refresh()
time.sleep(5)
stdscr.clear()
# Class selection
stdscr.addstr(0,0, "You can select from three classes, each with different stats. Below you can find the stats of each class")
stdscr.addstr(1,0, "Mage: health: 130, resistance: 5, defense: 2, attack: 10")
stdscr.addstr(2,0, "Knight: health: 180, resistance: 10, defense: 10, attack: 12")
stdscr.addstr(3,0, "Assassin: health: 70, resistance: 15, defense: 10, attack: 9")

stdscr.addstr(4,0, "Which class would you like? (CASE SENSITIVE, first letter, lowercase only) ")
stdscr.refresh()
classSelected: int | str = stdscr.getch()

# checking for class selected
if classSelected == 109:
    classSelected = "Mage"
elif classSelected == 107:
    classSelected = "Knight"
elif classSelected == 97:
    classSelected = "Assassin"
else: 
    exit()
    
createdPlayer = classSelected
    

if classSelected == "Mage":
    createdPlayer = Player(130, 5, 2, 10)
elif classSelected == "Knight":
    createdPlayer = Player(180, 10, 10, 12)
elif classSelected == "Assassin":
    createdPlayer = Player(70, 15, 10, 9)
else: 
    print("Wrong class selected, program will be terminated")
    exit()

'''
Basic game functionality starts here
'''


# Credits scene
def credits(stdscr) -> None:
    stdscr.clear()
    stdscr.addstr(0,4, "Congratulations!")
    time.sleep(2)
    stdscr.addstr(1,4, "You finished the game!")
    time.sleep(2)
    stdscr.addstr(2,4, "I hope you enjoyed ")
    
    stdscr.addstr(3,4, "Furry Femboy Sowrdsman idea - Charles")
    stdscr.addstr(4,4, "Code by me")
    stdscr.addstr(5,4, "Comments because mr.dartez forced me")
    


directions: list[str] = ["Left", "Right", "Forward", "Backward"]

# chooses direction for you
def chooseDirection(stdscr) -> None:
    curses.noecho()
    stdscr.clear()
    stdscr.addstr(0,0, "What direction would you like to go?")
    stdscr.addstr(1,0, "Left, Right, Forward, or Backward? (CASE SENSITIVE)")
    stdscr.addstr(2,0, "Please only input the first letter of the direction in lower case ")
    stdscr.refresh()
    while True:
        directionOfChoice: int = stdscr.getch()
        if directionOfChoice != -1:
            break
        
    if directionOfChoice == 102:
        move(stdscr, "Forward")
    elif directionOfChoice == 108:
        move(stdscr, "Left")
    elif directionOfChoice == 114:
        move(stdscr, "Right")
    elif directionOfChoice == 98:
        move(stdscr, "Backward")
    elif directionOfChoice != -1 :
        print("Invalid Direction")
        chooseDirection(stdscr)

'''
Movement function
'''
def move(stdscr, direction: str):
    if stepCounter[1] >= 20:
        findStructure(stdscr)
    
    lists = [
        "You trip on a twig", "You encounter an enemy", "You slip on moss", 
        "You encounter an enemy", "You find a secret chest", "You encounter an enemy"
    ]
    item = random.randrange(0, 5)
    
    if item in [1, 3, 5]:
        fightEnemy(stdscr, False)
    
    stdscr.clear()
    stdscr.addstr(4, 2, lists[item])
    stdscr.refresh()
    
    if item in [4]:
        gainedHealth = createdPlayer.resistance + createdPlayer.defense
        time.sleep(2)
        stdscr.clear()
        stdscr.addstr(4,2, f"You gained {math.floor(gainedHealth / 2)} health!")
        stdscr.refresh()
        createdPlayer.health += gainedHealth / 2
    
    if item in [0]:
        chance: float = random.random()
        if chance >= 0.50:
            stdscr.clear()
            stdscr.addstr(4, 0, "You fell :(")
            stdscr.refresh()
            createdPlayer.health -= 5
        else:
            stdscr.clear()
            stdscr.addstr(4, 0, "you managed to catch yourself, causing you to not take any damage")
            stdscr.refresh()
    
    if item in [2]:
        chance: float = random.random()
        if chance >= 0.7:
            stdscr.clear()
            stdscr.addstr(4, 0, "you managed to catch yourself, causing you to not take any damage")
            stdscr.refresh()
        else:
            stdscr.clear()
            stdscr.addstr(4,0, "you didn't catch yourself in time, you took 5 damage")
            stdscr.refresh()
            createdPlayer.health -= 5
            
    if stepCounter[0] == direction:
        stepCounter[1] += 1
    else:
        stepCounter[0] = direction
        stepCounter[1] = 1

    time.sleep(1)
    chooseDirection(stdscr)
    
def findStructure(stdscr) -> None:

    # Location functions    
    def blackSmith(stdscr) -> None:
        
        stdscr.clear()
        stdscr.addstr(4,4, "You walk into the black smith, what do you do? (u)pgrade (s)hop")
        stdscr.refresh()
        
        while True:
            keyPressed: int = stdscr.getch()
            
            # upgrades
            if keyPressed == 115:
                stdscr.clear()
                stdscr.addstr(4,4, "You talk to the blacksmith, he offers you weapon upgrades in exchange for a quest. Would you like to get a quest?")
                while True:
                    keyPressed: int = stdscr.getch()
                    if keyPressed == 121:
                        stdscr.clear()
                        stdscr.addstr(4,4, "Your quest is to slay, five of any monster. And no, previously slayed monsters, do not count")
                        questCounter[0] = True
                    break
                # don't forget the break statement
                break
            
            # shop
            if keyPressed == 117:
                stdscr.clear()
                stdscr.addstr(0,4, "You can purchase an attack upgrade for free here at this village.")
                stdscr.addstr(1,4, "Would you like a free upgrade? y or n")
                stdscr.refresh()
                while True:
                    keyPressed: int = stdscr.getch()
                    if keyPressed == 121:
                        createdPlayer.attack += 6
                        createdPlayer.health += 10
                        break
                    if keyPressed != 121 and keyPressed != -1:
                        break
                findStructure(stdscr)
                
    def suspisciousAlleyway(stdscr) -> None:
        stdscr.clear()
        stdscr.addstr(0,4, "You walk into a suspisoucs alleyway, there is a person standing there.")
        stdscr.refresh()
        time.sleep(2)
        stdscr.clear()
        stdscr.addstr(0,5, "He offers you a bag of 'fun' to cure your bordem. Do you take it? y or n")
        
        while True:
            keyPressed = stdscr.getch()
            
            if keyPressed == 121:
                stdscr.clear()
                stdscr.addstr(5,5, "You take the bag, and pour it all down your throat. You die of an overdose")
                stdscr.refresh()
                time.sleep(3)
                createdPlayer.health = 0
                exit()
            if keyPressed == 110:
                stdscr.clear()
                stdscr.addstr(5,5, "You polietly decline his offer. Which causes him to down the bag of 'fun'.")
                stdscr.addstr(5,6, "He dies of an overdose")
                stdscr.refresh()
                findStructure(stdscr)
                break
    
    def townHall(stdscr) -> None:
        stdscr.clear()
        stdscr.addstr(0, 0, "You stand outside the doors to the townhall.")
        stdscr.addstr(
            1, 0, "You hear a lot of commotion, and decide to go in.")
        stdscr.refresh()
        time.sleep(3)
        stdscr.clear()
        stdscr.addstr(0,0, "QUIET! Just because we're in immediate danger, doesn't mean you can run amock!")
        stdscr.addstr(1,0, "Hello, traveler, we have need of you.")
        stdscr.addstr(2,0, "On your way to the village, you saw enemies did you not?")
        stdscr.addstr(3,0, "This is because of the furry femboy swordsman leader in the cave above.")
        stdscr.addstr(4,0, "I would like for you to assist us,")
        stdscr.refresh()
        time.sleep(5)
        findStructure(stdscr)
        
    def cave(stdscr) -> None:
        stdscr.clear()
        stdscr.addstr(0, 0, "You stand in a dark cave, you hear a loud growling sound.")
        stdscr.refresh()
        fightEnemy(stdscr, True)
        credits(stdscr)
        exit()
        
    
    if stepCounter[1] == 20:
        stdscr.addstr(4,0, "You encounter a village, what do you do? You can visit the following the buildings: (b)lack smith, (t)own hall, (s)uspicoius alleyway, (c)ave")
        stdscr.refresh()
        while True:
            keyPressed: int = stdscr.getch()
            if keyPressed == 98:
                blackSmith(stdscr)
                break
            elif keyPressed == 116:
                townHall(stdscr)
                break
            elif keyPressed == 115:
                suspisciousAlleyway(stdscr)
                break
            elif keyPressed == 99:
                cave(stdscr)
                break

    
# kind of self explanatory :3
def fightEnemy(stdscr, cave: bool) -> None:
    
    # kind of self explanatory :3
    def Attack(genEnemy, stdscr, cave: bool) -> None:
        playerAttack = createdPlayer.attack
        enemyAttack = genEnemy.attack
        enemyHealth = genEnemy.health
        playerHealth = createdPlayer.health
        chance: int = random.random()
        if chance > 0.5:
            enemyHealth = enemyHealth - playerAttack
            genEnemy.health = enemyHealth
            if enemyHealth > 0:
                stdscr.clear()
                stdscr.addstr(4,4, f"you hit it, the enemy's health is: {enemyHealth}")
                stdscr.refresh()
                time.sleep(2)
            else:
                if questCounter[0] == True:
                    questCounter[1] += 1
                stdscr.clear()
                stdscr.addstr(4,4, "Enemy Desimated")
                stdscr.refresh()
                time.sleep(2)
                if cave == False:
                    chooseDirection(stdscr)
                else: 
                    credits(stdscr)
        else:
            playerHealth = playerHealth - enemyAttack
            createdPlayer.health = playerHealth
            stdscr.clear()
            
            if playerHealth > 0:
                stdscr.addstr(4,4, f"you missed, your health is: {playerHealth}")
                stdscr.refresh()
            else:
                stdscr.addstr(4,4, "you died a horrible gorey death we can't describe due to content restrictions :(")
                stdscr.refresh()
                time.sleep(1)
                exit()
            time.sleep(2)
        
        if enemyHealth > 0:
            while True:
                keyPressed = stdscr.getch()
                if keyPressed == 97:
                    if cave == True:
                        Attack(genEnemy, stdscr, True)
                    else:
                        Attack(genEnemy, stdscr, False)
                if keyPress == 100:
                    Dodge(createdEnemy, stdscr)
                if keyPress == 112:
                    Parry(createdEnemy, stdscr)
            
    def Dodge(genEnemy,stdscr, cave: bool) -> None:
        enemyAttack = genEnemy.attack
        playerHealth = createdPlayer.health
        stdscr.clear()
        chance = random.random()
        if chance > 0.5:
            stdscr.addstr(4,4, "You dodged")
        else:
            stdscr.addstr(4,4, "You didn't dodge in time")
            if playerHealth > 0:
                playerHealth = playerHealth - enemyAttack
                createdPlayer.health = playerHealth
                time.sleep(1)
                stdscr.clear()
                stdscr.addstr(4,4, f"You now have {playerHealth} total health")
                stdscr.refresh()
                time.sleep(1)
            else:
                stdscr.addstr(4,4, "you died a horrible gorey death we can't describe due to content restrictions :(")
                stdscr.refresh()
                time.sleep(1)
                exit()
                
    def Parry(genEnemy, stdscr, cave: bool) -> None:
        enemyAttack = genEnemy.attack
        playerHealth = createdPlayer.health
        
        chance = random.random()
        if chance > 0.5:
            stdscr.clear()
            stdscr.addstr(4,4, "You parried")
            stdscr.refresh()
        else:
            if playerHealth > 0:
                playerHealth = playerHealth - enemyAttack
                createdPlayer.health = playerHealth
                
                stdscr.clear()
                stdscr.addstr(4,4, f"You didn't parry in time, you now have {playerHealth} health remaining")
                stdscr.refresh()
            else:
                stdscr.addstr(4,4, "you died a horrible gorey death we can't describe due to content restrictions :(")
                stdscr.refresh()
                time.sleep(100)
                exit()
    
    if cave == True:
        stdscr.clear()
        stdscr.addstr(4, 0, "You encounter a furry femboy swordsman leader :3, what do you do?")
        stdscr.refresh()
        time.sleep(2)

        stdscr.clear()
        stdscr.addstr(4, 0, "a)ttack d)odge p)arry")
        stdscr.refresh()
        time.sleep(1)

        createdEnemy = Enemy(200, 10, 8, 20)
        while True:
            keyPress: int = stdscr.getch()
        
            if keyPress == 97:
                Attack(createdEnemy, stdscr, cave)
            if keyPress == 100:
                Dodge(createdEnemy, stdscr, cave)
            if keyPress == 112:
                Parry(createdEnemy, stdscr, cave)
    
    enemyList: list[str] = ["Slime", "Turtle", "Bird", "Zombie", "Spider", "Archer", "Furry Femboy :3 swordsman UwU"]
    item: str = random.choice(enemyList)
    choiceOfEnemy: None | str = None
    
    if item == "Slime":
        choiceOfEnemy = "Slime"
        
    elif item == "Turtle":
        choiceOfEnemy = "Turtle"
        
    elif item == "Bird":
        choiceOfEnemy = "Bird"
        
    elif item == "Zombie":
        choiceOfEnemy = "Zombie"
        
    elif item == "Spider":
        choiceOfEnemy = "Spider"
        
    elif item == "Archer":
        choiceOfEnemy = "Archer"
        
    else:
        choiceOfEnemy = "Furry Femboy :3 swordsman UwU"
    
        
    createdEnemy = None
    
    enemyValues = {
        "Slime":{
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 2,
        },
        "Turtle": {
            "health": 30,
            "resistance": 5,
            "defense": 5,
            "attack": 5,
        },
        "Bird": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 10,
        },
        "Zombie": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 15,
        },
        "Spider": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 5,
        },
        "Archer": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 10,
        },
        "Furry Femboy :3 swordsman UwU": {
            "health": 150,
            "resistance": 10,
            "defense": 8,
            "attack": 20,
        }
    }
    
    createdEnemy = Enemy(enemyValues[item]["health"], enemyValues[item]["resistance"], enemyValues[item]["defense"], enemyValues[item]["attack"])
    
    stdscr.clear()
    stdscr.addstr(4,4, f"You encounter a(n) {choiceOfEnemy}.")
    stdscr.refresh()
    time.sleep(3)
    
    stdscr.clear()
    stdscr.addstr(4,4, "What do you do?")
    stdscr.refresh()
    time.sleep(2)
    
    stdscr.clear()
    stdscr.addstr(4,4, "a)ttack d)odge p)arry")
    stdscr.refresh()
    time.sleep(1)
    
    while True:
        keyPress: int = stdscr.getch()
        
        if keyPress == 97:
            Attack(createdEnemy, stdscr, False)
        if keyPress == 100:
            Dodge(createdEnemy, stdscr)
        if keyPress == 112:
            Parry(createdEnemy, stdscr)


'''
Furry swordsman UwU -charles
comments -mr.dartez forced me
'''

    
# INCLUDE THIS LINE AT THE END OF THE CODE, AND CREATE AN ALL ENCOMPASSING FUNCTION TO HANDLE LOGIC

def main(stdscr) -> None:
    stdscr.clear()
    stdscr.timeout(100)
    stdscr.keypad(False)
    curses.noecho()
    while True:
        if createdPlayer.health > 0:
            chooseDirection(stdscr)
        else: 
            break
    
curses.wrapper(main)
