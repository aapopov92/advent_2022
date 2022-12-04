# https://adventofcode.com/2022/day/2

choice_prices = {
	"X": 1, # rock
	"Y": 2, # paper
	"Z": 3 # scissors
}

round_outcomes = {
	"X": {"A": 3, "B": 0, "C": 6},
	"Y": {"A": 6, "B": 3, "C": 0},
	"Z": {"A": 0, "B": 6, "C": 3},
}

score = 0

with open("input.txt", "r") as file:
	for line in file:
		opponent_choice, your_choice = line.split()
		score += choice_prices[your_choice] + round_outcomes[your_choice][opponent_choice]

print(score)


