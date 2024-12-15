package main

import (
	"fmt"
	"os"
)

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
			fmt.Println("")
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
				player.Attack += 1
				player.Health -= 1
			case "Right", "right", "R", "r":
				player.Attack += 1
				player.Health -= 1
			case "Forward", "forward", "F", "f":
				player.Attack += 1
				player.Health -= 1
			case "Backward", "backward", "B", "b":
				player.Attack += 1
				player.Health -= 1
			default:
				continue
			}
		}
	}
	player.Health = 0
}
