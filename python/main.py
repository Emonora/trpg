import random
import curses
import time

stdscr = curses.initscr()
stepCounter = ["Right", 18]
questCounter = [False, 0]
pneumonoultramicroscopicsilicovolcanoconiosis: bool = False

class Player:
    def __init__(self, health, resistance, defense, attack, attackSpeed):
        self.health = health
        self.resistance = resistance
        self.defense = defense
        self.attack = attack
        self.attackSpeed = attackSpeed
    def __str__(self):
        returned = f"Health: {self.health}, Resistance: {self.resistance}, Defense: {self.defense}, Attack: {self.attack}, Attack speed: {self.attackSpeed}"
        return returned

class Enemy:
    def __init__(self, health, resistance, defense, attack, attackSpeed):
        self.health = health
        self.resistance = resistance
        self.defense = defense
        self.attack = attack
        self.attackSpeed = attackSpeed
    def __str__(self):
        returned = f"Health: {self.health}, Resistance: {self.resistance}, Defense: {self.defense}, Attack: {self.attack}, Attack speed: {self.attackSpeed}"
        return returned

playerType: list[str] = ["Mage", "Knight", "Assassin"]
stdscr.addstr(4, 4, "Welcome to TRPG! A fully open source, souls-like text based rpg. ")
stdscr.refresh()
time.sleep(1)
stdscr.clear()
stdscr.addstr(4,4, "If you haven't already, please extend your output/terminal window to the maxium width, for best gameplay")
stdscr.refresh()
time.sleep(5)
stdscr.clear()
stdscr.addstr(0,0, "You can select from three classes, each with different stats. Below you can find the stats of each class")
stdscr.addstr(1,0, "Mage: health: 100, resistance: 5, defense: 2, attack: 5, attack speed: 2")
stdscr.addstr(2,0, "Knight: health: 150, resistance: 10, defense: 10, attack: 10, attack speed: 2")
stdscr.addstr(3,0, "Assassin: health: 50, resistance: 0, defense: 0, attack: 5, attack speed: 22")

stdscr.addstr(4,0, "Which class would you like? (CASE SENSITIVE, first letter, lowercase only) ")
stdscr.refresh()
classSelected: int | str = stdscr.getch()

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
    createdPlayer = Player(100, 5, 2, 5, 2)
elif classSelected == "Knight":
    createdPlayer = Player(150, 10, 10, 10, 2)
elif classSelected == "Assassin":
    createdPlayer = Player(50, 0, 0, 5, 22)
else: 
    print("Wrong class selected, program will be terminated")
    exit()

'''
Basic game functionality starts here
'''

directions: list[str] = ["Left", "Right", "Forward", "Backward"]

# chooses direction for you
def chooseDirection(stdscr) -> None:
    curses.noecho()
    stdscr.clear()
    stdscr.addstr(0,0, "What direction would you like to go?")
    stdscr.addstr(1,0, "Left, Right, Forward, or Backward? (CASE SENSITIVE)")
    stdscr.addstr(2,0, "Please only input the first letter of the direction in lower case ")
    stdscr.addstr(10,0, "If the game freezes, please press a")
    stdscr.refresh()
    while True:
        directionOfChoice: int = stdscr.getch()
        if directionOfChoice != -1:
            break
        
    if directionOfChoice == 102:
        moveForward(stdscr)
    elif directionOfChoice == 108:
        moveLeft(stdscr)
    elif directionOfChoice == 114:
        moveRight(stdscr)
    elif directionOfChoice == 98:
        moveBackward(stdscr)
    elif directionOfChoice != -1 :
        print("Invalid Direction")
        chooseDirection(stdscr)

'''
Movement functions
'''

def moveForward(stdscr) -> None:
    list: [str] = ["You trip on a twig", "You encouter an enemy", "You slip on moss", "You encouter an enemy", "You find a secret chest", "You encouter an enemy"]
    item: int = random.randrange(0, 5, 1)
    stdscr.addstr(4,2, str(list[item]))
    stdscr.refresh()
    if item == 1 or item == 3 or item == 5:
        stepCounter[1] = stepCounter[1] + 1
        fightEnemy(stdscr)
    if stepCounter[0] == "Forward":
        stepCounter[1] = stepCounter[1] + 1
    else:
        stepCounter[0] = "Forward"
        stepCounter[1] = 1

    time.sleep(1)

def moveBackward(stdscr) -> None:
    list: list[str] = ["You trip on a twig", "You encouter an enemy", "You slip on moss", "You encounter an enemy", "You fall backwards", "You encouter an enemy", "You find a secret chest", "You encouter an enemy"]
    item: int = random.randrange(0, 7, 1)
    stdscr.addstr(4,2, str(list[item]))
    stdscr.refresh()
    if item == 1 or item == 3 or item == 5 or item == 7:
        fightEnemy(stdscr)
    if stepCounter[0] == "Backward":
        stepCounter[1] = stepCounter[1] + 1
    else:
        stepCounter[0] = "Backward"
        stepCounter[1] = 1
    
    time.sleep(1)


def moveLeft(stdscr) -> None:
    list: list[str] = ["You trip on a twig", "You encouter an enemy", "You slip on moss", "You encouter an enemy", "You find a secret chest", "You encouter an enemy"]
    item: int = random.randrange(0, 5, 1)
    stdscr.addstr(4, 2, str(list[item]))
    stdscr.refresh()
    if item == 1 or item == 3 or item == 5:
        fightEnemy(stdscr)
    if stepCounter[0] == "Left":
        stepCounter[1] = stepCounter[1] + 1
    else:
        stepCounter[0] = "Left"
        stepCounter[1] = 1
    
    time.sleep(1)


def moveRight(stdscr) -> None:
    list: list[str] = ["You trip on a twig", "You encouter an enemy", "You slip on moss", "You encouter an enemy", "You find a secret chest", "You encouter an enemy"]
    item: int = random.randrange(0, 5, 1)
    
    if stepCounter[1] >= 20:
        findStructure(stdscr)
    
    stdscr.addstr(4, 2, str(list[item]))
    stdscr.refresh()
    if item == 1 or item == 3 or item == 5:
        fightEnemy(stdscr)
    if stepCounter[0] == "Right":
        stepCounter[1] = stepCounter[1] + 1
    else:
        stepCounter[0] = "Right"
        stepCounter[1] = 1
    
    time.sleep(1)

def findStructure(stdscr) -> None:

    # Location functions    
    def blackSmith(stdscr) -> None:
        
        stdscr.clear()
        stdscr.addstr(4,4, "You walk into the black smith, what do you do? (u)pgrade (s)hop")
        stdscr.refresh()
        
        while True:
            keyPressed: int = stdscr.getch()
            
            # upgrades
            if keyPressed == 117:
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
            if keyPressed == 115:
                stdscr.clear()
                stdscr.addstr(0,4, "You can purchase an attack upgrade for free here at this village.")
                
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
        stdscr.addstr(0,0, "You stand outside the doors to the townhall.")
        stdscr.addstr(1,0, "You hear a lot of commotion, and decide to go in.")
        stdscr.refresh()
        time.sleep(3)
        stdscr.clear()
        
    
    if stepCounter[1] == 20:
        stdscr.addstr(4,0, "You encounter a village, what do you do? You can visit the following the buildings: (b)lack smith, (t)own hall, (s)uspicoius alleyway, (c)ave")
        stdscr.refresh()
        while True:
            keyPressed: int = stdscr.getch()
            if keyPressed == 98:
                blackSmith(stdscr)
                break
            elif keyPressed == 116:
                # townHall()
                break
            elif keyPressed == 115:
                suspisciousAlleyway(stdscr)
                break
            elif keyPressed == 99:
                # cave()
                break

    
# kind of self explanatory :3
def fightEnemy(stdscr) -> None:
    
    # kind of self explanatory :3
    def Attack(genEnemy, stdscr) -> None:
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
                chooseDirection(stdscr)
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
                    Attack(genEnemy, stdscr)
                if keyPress == 100:
                    Dodge(createdEnemy, stdscr)
                if keyPress == 112:
                    Parry(createdEnemy, stdscr)
            
    def Dodge(genEnemy,stdscr) -> None:
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
                
    def Parry(genEnemy, stdscr) -> None:
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
                
    enemyList: [str] = ["Slime", "Turtle", "Bird", "Zombie", "Spider", "Archer", "Furry Femboy :3 swordsman UwU"]
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
            "attackSpeed": 5
        },
        "Turtle": {
            "health": 30,
            "resistance": 5,
            "defense": 5,
            "attack": 5,
            "attackSpeed": 1
        },
        "Bird": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 10,
            "attackSpeed": 2
        },
        "Zombie": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 15,
            "attackSpeed": 2
        },
        "Spider": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 5,
            "attackSpeed": 2
        },
        "Archer": {
            "health": 10,
            "resistance": 5,
            "defense": 5,
            "attack": 10,
            "attackSpeed": 2
        },
        "Furry Femboy :3 swordsman UwU": {
            "health": 150,
            "resistance": 10,
            "defense": 8,
            "attack": 20,
            "attackSpeed": 4
        }
    }
    
    createdEnemy = Enemy(enemyValues[item]["health"], enemyValues[item]["resistance"], enemyValues[item]["defense"], enemyValues[item]["attack"], enemyValues[item]["attackSpeed"])
    
    stdscr.clear()
    stdscr.addstr(4,4, f"You encounter a {choiceOfEnemy}.")
    stdscr.refresh()
    time.sleep(3)
    
    stdscr.clear()
    stdscr.addstr(4,4, "What do you do?")
    stdscr.refresh()
    time.sleep(2)
    
    stdscr.clear()
    stdscr.addstr(4,4, "A)ttack D)odge P)arry")
    stdscr.refresh()
    time.sleep(1)
    
    while True:
        keyPress: int = stdscr.getch()
        
        if keyPress == 97:
            Attack(createdEnemy, stdscr)
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
