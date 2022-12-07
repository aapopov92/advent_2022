#  https://adventofcode.com/2022/day/4
accumulator = 0
with open("input.txt", "r") as file:
    for line in file:
        first_elf_range, second_elf_range = line.strip().split(",")
        first_elf_range_start, first_elf_range_finish = first_elf_range.split("-")
        second_elf_range_start, second_elf_range_finish = second_elf_range.split("-")
        if (
            int(first_elf_range_start) <= int(second_elf_range_start) <= int(first_elf_range_finish)        # ...|------|... first
            and int(second_elf_range_start) <= int(first_elf_range_finish) <= int(second_elf_range_finish)  # ....|------|.. second
        ) or (
            int(second_elf_range_start) <= int(first_elf_range_start) <= int(second_elf_range_finish)       # ...|------|... first
            and int(first_elf_range_start) <= int(second_elf_range_finish) <= int(first_elf_range_finish)   # ..|------|.... second
        ) or (
            int(first_elf_range_start) <= int(second_elf_range_start)                                       # ....|------|.. first
            and int(first_elf_range_finish) >= int(second_elf_range_finish)                                 # ......|---|... second
        ) or (
            int(first_elf_range_start) >= int(second_elf_range_start)                                       # ....|--|..... first
            and int(first_elf_range_finish) <= int(second_elf_range_finish)                                 # ...|------|.. second
        ):
            accumulator += 1
        else:
            print(first_elf_range, second_elf_range)

print(accumulator)
