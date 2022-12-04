# https://adventofcode.com/2022/day/2

outcome_prices = {
	"X": 0, # lose
	"Y": 3, # draw
	"Z": 6 # win
}

choice_prices = {
	"X": {"A": 3, "B": 1, "C": 2},
	"Y": {"A": 1, "B": 2, "C": 3},
	"Z": {"A": 2, "B": 3, "C": 1},
}

score = 0

with open("input.txt", "r") as file:
	for line in file:
		opponent_choice, your_outcome = line.split()
		score += outcome_prices[your_outcome] + choice_prices[your_outcome][opponent_choice]

print(score)


