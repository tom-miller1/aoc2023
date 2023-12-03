import re
from collections import defaultdict

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def calculate_part_sum(input):
    part_numbers = defaultdict(list)
    symbol_locations = defaultdict(list)
    for line_no, line in enumerate(input.splitlines(), start=1):
        # pad line with non-symbols to avoid negative indexing
        line = "." + line + "."

        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            part_numbers[line_no].append((number.span(), number.group()))

        symbols = re.finditer(r"[^\d.]", line)
        for symbol in symbols:
            symbol_locations[line_no].append(symbol.span()[0])

    # check part numbers for symbol-adjacency
    part_sum = 0
    for row, entries in part_numbers.items():
        for entry in entries:
            x_span = range(entry[0][0] - 1, entry[0][1] + 1)
            # check 3 rows near this one for markers
            for y in range(row - 1, row + 2):
                if y in symbol_locations:
                    for x in symbol_locations[y]:
                        if x in x_span:
                            part_sum += int(entry[1])

    return part_sum


def calculate_gear_ratio(input):
    part_numbers = defaultdict(list)
    gear_locations = defaultdict(list)
    for line_no, line in enumerate(input.splitlines(), start=1):
        # pad line with non-symbols to avoid negative indexing
        line = "." + line + "."

        numbers = re.finditer(r"\d+", line)
        for number in numbers:
            part_numbers[line_no].append((number.span(), number.group()))

        gears = re.finditer(r"\*", line)
        for gear in gears:
            gear_locations[line_no].append(gear.span()[0])

    # check gears for part number adjacency
    gear_ratio_sum = 0
    for row, x_locs in gear_locations.items():
        for x_loc in x_locs:
            maybe_ratio = []
            # check 3 rows near this one for part numbers
            for y in range(row - 1, row + 2):
                if y in part_numbers:
                    for x, number in part_numbers[y]:
                        x_span = range(x[0] - 1, x[1] + 1)
                        if x_loc in x_span:
                            maybe_ratio.append(int(number))
            print(maybe_ratio)
            if len(maybe_ratio) == 2:
                gear_ratio_sum += maybe_ratio[0] * maybe_ratio[1]

    return gear_ratio_sum


if __name__ == '__main__':
    test_sum = calculate_part_sum(test_input)
    print(f"Part 1 test: {test_sum}")

    test_ratio = calculate_gear_ratio(test_input)
    print(f"Part 2 test: {test_ratio}")

    with open("aoc-input3.txt", "rt") as f:
        data = f.read()

    part1_sum = calculate_part_sum(data)
    part2_sum = calculate_gear_ratio(data)
    print(f"Part 1: {part1_sum}")
    print(f"Part 2: {part2_sum}")
