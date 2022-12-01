top_calories = []
with open('input.txt') as file:
	running_sum = 0
	for line in file:
		if line != '\n':
			running_sum += int(line)
		else:
			top_calories = sorted(top_calories + [running_sum], reverse=True)[0:3]
			running_sum = 0

print(sum(top_calories))