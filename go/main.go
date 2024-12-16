/*
	Everything within this file, should function similarly to the original python version, with a few exceptions.
	The main difference is that this is written in golang, and the python version is written in python.
	This file was my first project in golang, and I'm still learning the language.
*/

package main

import (
	"fmt"
	"math/rand/v2"
	"os"
)

var cave bool = false
var questCounter = [...]interface{}{false, 0}
var stepCounter = [...]interface{}{"Direction", 0}
var pneumonoultramicroscopicsilicovolcanoconiosis bool = false

type Player struct {
	Health     int
	Resistance int
	Defense    int
	Attack     int
}

type Enemy struct {
	Health     int
	Resistance int
	Defense    int
	Attack     int
}

func startGame() Player {
	fmt.Println("Welcome to trpg! A simple rpg game written in golang")
	fmt.Println("You can pick a class to play below.")
	fmt.Println("1. Knight: 180 health, 10 resistance, 10 defense, 12 attack")
	fmt.Println("2. Mage: 130 health, 5 resistance, 2 defense, 10 attack")
	fmt.Println("3. Assassin: 70 health, 15 resistance, 10 defense, 9 attack")
	fmt.Println("Which class would you like to play? (CASE SENSITIVE)")
	fmt.Println("")

	var classSelected string
	_, err := fmt.Scanln(&classSelected)
	var player Player = Player{
		Health:     0,
		Resistance: 0,
		Defense:    0,
		Attack:     0,
	}
	if err != nil {
		fmt.Println("Invalid input")
		os.Exit(1)
	} else {
		switch classSelected {
		case "Knight", "knight", "1", "1.":
			fmt.Println("You chose the knight class")
			fmt.Println("You have 180 health, 10 resistance, 10 defense, 12 attack")

			player = Player{
				Health:     180,
				Resistance: 10,
				Defense:    10,
				Attack:     12,
			}

			return player
		case "Mage", "mage", "2", "2.":
			fmt.Println("You chose the mage class")
			fmt.Println("You have 130 health, 5 resistance, 2 defense, 10 attack")

			player = Player{
				Health:     130,
				Resistance: 5,
				Defense:    2,
				Attack:     10,
			}

			return player
		case "Assassin", "assassin", "3", "3.":
			fmt.Println("You chose the assassin class")
			fmt.Println("You have 70 health, 15 resistance, 10 defense, 9 attack")

			player = Player{
				Health:     70,
				Resistance: 15,
				Defense:    10,
				Attack:     9,
			}

			return player
		default:
			fmt.Println("Invalid class selected")
			os.Exit(1)
		}
	}
	return player
}

func generateEnemy() Enemy {
	enemy := Enemy{
		Health:     rand.IntN(100),
		Resistance: rand.IntN(100),
		Defense:    rand.IntN(100),
		Attack:     rand.IntN(100),
	}
	return enemy
}

// fightEnemy function, including all sub-functions
func fightEnemy(player Player, enemy Enemy) {
	Attack := func(player *Player, enemy *Enemy) {
		playerAttack := player.Attack
		enemyAttack := enemy.Attack
		enemyHealth := enemy.Health
		playerHealth := player.Health

		chance := rand.Float64()

		if chance > 0.5 {
			enemyHealth = enemyHealth - playerAttack
			enemy.Health = enemyHealth
			if enemyHealth > 0 {
				fmt.Println("You hit it, the enemy's health is:", enemyHealth)
			} else {
				fmt.Println("Enemy Desimated")
				return
			}
		} else {
			playerHealth = playerHealth - enemyAttack
			player.Health = playerHealth
			if playerHealth > 0 {
				fmt.Println("you missed, your health is:", playerHealth)
			} else {
				fmt.Println("you died a horrible gorey death we can't describe due to content restrictions :(")
				os.Exit(1)
			}
		}
	}

	Dodge := func(player *Player, enemy *Enemy) {
		enemyAttack := enemy.Attack
		playerHealth := player.Health
		chance := rand.Float64()
		if chance > 0.5 {
			fmt.Println("You dodged")
		} else {
			fmt.Println("You didn't dodge in time")
			if playerHealth > 0 {
				playerHealth = playerHealth - enemyAttack
				player.Health = playerHealth
				fmt.Println("You now have ", playerHealth, " total health")
			} else {
				fmt.Println("you died a horrible gorey death we can't describe due to content restrictions :(")
				os.Exit(1)
			}
		}
	}

	Parry := func(player *Player, enemy *Enemy) {
		enemyAttack := enemy.Attack
		enemyHealth := enemy.Health
		playerHealth := player.Health
		playerAttack := player.Attack
		chance := rand.Float64()
		if chance > 0.5 {
			fmt.Println("You parried")
			enemyHealth = enemyHealth - playerAttack
			enemy.Health = enemyHealth
		} else {
			if playerHealth > 0 {
				playerHealth = playerHealth - enemyAttack
				player.Health = playerHealth
				fmt.Println("You didn't parry in time, you now have", playerHealth, "health remaining")
			} else {
				fmt.Println("you died a horrible gorey death we can't describe due to content restrictions :(")
				os.Exit(1)
			}
		}
	}

	var selectedAction string

	createdEnemyName := "Furry Femboy :3 swordsman UwU"

	fmt.Println("")
	fmt.Println("You encounter a(n)", createdEnemyName, "what do you do?")
	fmt.Println("")

	for enemy.Health > 0 {
		fmt.Println("")
		fmt.Println("a)ttack d)odge p)arry")
		fmt.Println("")
		fmt.Scanln(&selectedAction)
		fmt.Println("")

		switch selectedAction {
		case "a", "A", "attack", "Attack":
			Attack(&player, &enemy)
		case "d", "D", "dodge", "Dodge":
			Dodge(&player, &enemy)
		case "p", "P", "parry", "Parry":
			Parry(&player, &enemy)
		}
	}

}

func findStructure(player *Player) {
	val, ok := stepCounter[1].(int)
	if !ok {
		fmt.Println("Error: stepCounter[1] is not an int")
		os.Exit(1)
	}
	if val >= 20 {
		fmt.Println("You encounter a village! You have four places to choose from")
		fmt.Println("1. Village Blacksmith")
		fmt.Println("2. Village Town Hall")
		fmt.Println("3. Village Cave")
		fmt.Println("4. Village Alley")
		fmt.Println("")
		var choice string
		_, err := fmt.Scanln(&choice)
		if err != nil {
			fmt.Println("Invalid input")
			os.Exit(1)
		} else {
			switch choice {
			case "1", "1.":
				fmt.Println("You choose the blacksmith")
				fmt.Println("You walk into the blacksmith, and you see a man hammering away at a piece of metal")
				fmt.Println("")
				fmt.Println("The man offers you a piece of metal, and you take it. This increases your damgee by 6")
				player.Attack += 6
			case "2", "2.":
				fmt.Println("You choose the town hall")
				stepCounter[1] = 1
			case "3", "3.":
				fmt.Println("You choose the cave")
				stepCounter[1] = 1
			case "4", "4.":
				fmt.Println("You choose the alley")
				stepCounter[1] = 1
			default:
				fmt.Println("Invalid choice")
				os.Exit(1)
			}
		}

	}
}

// movement function
func move(player Player, direction string) {

	chooseEvent := func() string {
		possibleEvents := []string{
			"You trip on a twig",
			"You slip on some moss",
			"You find a secret chest",
			"You encounter an enemy",
			"You encounter an enemy",
			"You encounter an enemy",
		}
		return possibleEvents[rand.IntN(len(possibleEvents))]
	}

	if player.Health > 0 {
		fmt.Println("")
		switch direction {
		case "Left", "left", "L", "l":
			var chosenEvent string = chooseEvent()
			if chosenEvent != "You encounter an enemy" {
				fmt.Println(chosenEvent)
				if stepCounter[0] != "Left" {
					stepCounter[0] = "Left"
					stepCounter[1] = 1
				} else {
					val, ok := stepCounter[1].(int)
					if !ok {
						fmt.Println("Error: stepCounter[1] is not an int")
						os.Exit(1)
					}
					val++
					stepCounter[1] = val
				}
			} else {
				genEnemy := generateEnemy()
				fightEnemy(player, genEnemy)
			}
		case "Right", "right", "R", "r":
			var chosenEvent string = chooseEvent()
			if chosenEvent != "You encounter an enemy" {
				fmt.Println(chosenEvent)
				if stepCounter[0] != "Right" {
					stepCounter[0] = "Right"
					stepCounter[1] = 1
				} else {
					val, ok := stepCounter[1].(int)
					if !ok {
						fmt.Println("Error: stepCounter[1] is not an int")
						os.Exit(1)
					}
					val++
					stepCounter[1] = val
				}
			} else {
				genEnemy := generateEnemy()
				fightEnemy(player, genEnemy)
			}
		case "Forward", "forward", "F", "f":
			var chosenEvent string = chooseEvent()
			if chosenEvent != "You encounter an enemy" {
				fmt.Println(chosenEvent)
				if stepCounter[0] != "Forward" {
					stepCounter[0] = "Forward"
					stepCounter[1] = 1
				} else {
					val, ok := stepCounter[1].(int)
					if !ok {
						fmt.Println("Error: stepCounter[1] is not an int")
						os.Exit(1)
					}
					val++
					stepCounter[1] = val
				}
			} else {
				genEnemy := generateEnemy()
				fightEnemy(player, genEnemy)
			}
		case "Backward", "backward", "B", "b":
			var chosenEvent string = chooseEvent()
			if chosenEvent != "You encounter an enemy" {
				fmt.Println(chosenEvent)
				if stepCounter[0] != "Backward" {
					stepCounter[0] = "Backward"
					stepCounter[1] = 1
				} else {
					val, ok := stepCounter[1].(int)
					if !ok {
						fmt.Println("Error: stepCounter[1] is not an int")
						os.Exit(1)
					}
					val++
					stepCounter[1] = val
				}
			} else {
				genEnemy := generateEnemy()
				fightEnemy(player, genEnemy)
			}
		default:
			fmt.Println("Invalid direction")
			os.Exit(1)
		}
	}
}

// main function, which is the entry point of the program
func main() {

	var player Player = startGame()
	for {
		fmt.Println("")
		fmt.Println("What direction would you like to go?")
		fmt.Println("Left, Right, Forward, or Backward? (CASE SENSITIVE) ")
		fmt.Println("")

		var direction string
		_, err := fmt.Scanln(&direction)

		if err != nil {
			fmt.Println("Invalid input")
			os.Exit(1)
		} else {
			switch direction {
			case "Left", "left", "L", "l":
				move(player, direction)
			case "Right", "right", "R", "r":
				move(player, direction)
			case "Forward", "forward", "F", "f":
				move(player, direction)
			case "Backward", "backward", "B", "b":
				move(player, direction)
			default:
				continue
			}
		}
	}
}
