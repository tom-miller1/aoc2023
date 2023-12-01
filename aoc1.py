DIGITS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
NUM_MAP = {
    # tricky merged digit words
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "98",
    # digit words
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pt1_total = 0
pt2_total = 0

with open("aoc1.txt", "rt") as f:
    for line in f:
        # part 1
        numbers = [c for c in line if c in DIGITS]
        pt1_total += int(f"{numbers[0]}{numbers[-1]}")

        # part 2
        line = line.lower().strip()
        for word, digit in NUM_MAP.items():
            line = line.replace(word, digit)
        numbers = [c for c in line if c in DIGITS]
        pt2_total += int(f"{numbers[0]}{numbers[-1]}")

print(f"Part 1: {pt1_total}")
print(f"Part 2: {pt2_total}")
