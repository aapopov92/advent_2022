# read initial stacks from input
raw_stacks = []
with open("input.txt", "r") as file:
	for line in file:
		if line == '\n':
			break
		else:
			raw_stacks.append(line[:-1])  # remove newline at the end

stack_indexes = [raw_stacks[-1].index(item) for item in raw_stacks[-1].split()]  # calculate indexes for stack elements

stacks = [[] for _ in stack_indexes]  # pre-create list of stacks
for line in raw_stacks[:-1][::-1]:  # go through stack lines in reversed order, without last line with stack numbers
	for stack_n, idx in enumerate(stack_indexes):
		if line[idx] != ' ':
			stacks[stack_n].append(line[idx])

with open("input.txt", "r") as file:
	for line in file:
		if line.startswith('move'):
			_, amount, _, src, _, dst = line.strip().split()
			reminder, to_move = stacks[int(src) - 1][:-int(amount)], stacks[int(src) - 1][-int(amount):]
			stacks[int(src) - 1] = reminder
			stacks[int(dst) - 1] += to_move

print(''.join([stack[-1] for stack in stacks]))