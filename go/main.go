package main

import (
	"fmt"
	"time"
)

type Player struct {
	Health     int
	Resistance int
	Defense    int
	Attack     int
}

func main() {
	var player Player

	init := func() {
		fmt.Println("Welcome to trpg, a souls like rpg originally written in python, ported to go!")
		time.Sleep(time.Second * 2)
		fmt.Println("You can select from three classes, each with different stats. Below you can find the stats of each class")
		time.Sleep(time.Second * 2)
		fmt.Println("Mage: health: 130, resistance: 5, defense: 2, attack: 10")
		fmt.Println("Knight: health: 180, resistance: 10, defense: 10, attack: 12")
		fmt.Println("Assassin: health: 70, resistance: 15, defense: 10, attack: 9")
		time.Sleep(time.Second * 2)
		fmt.Println("Which class would you like? (CASE SENSITIVE)")
		var classSelected string
		fmt.Scanln(&classSelected)

		if classSelected == "Mage" {
			fmt.Println("You selected the mage class")
			player.Health = 130
			player.Resistance = 5
			player.Defense = 2
			player.Attack = 10
			fmt.Println(player)
		} else if classSelected == "Knight" {
			fmt.Println("You selected the knight class")
			player.Health = 180
			player.Resistance = 10
			player.Defense = 10
			player.Attack = 12
		} else if classSelected == "Assassin" {
			fmt.Println("You selected the assassin class")
			player.Health = 70
			player.Resistance = 15
			player.Defense = 10
			player.Attack = 9
		} else {
			fmt.Println("Invalid class selected, please try again")
			main()
		}
	}

	init()

	fmt.Println("Welcome to the game!")
}
