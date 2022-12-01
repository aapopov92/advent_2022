# https://adventofcode.com/2022/day/1
max_calories = 0
with open('input.txt') as file:
	running_sum = 0
	for line in file:
		if line != '\n':
			running_sum += int(line)
		else:
			max_calories = max(max_calories, running_sum)
			running_sum = 0

print(max_calories)