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
DIGIT_MAP = {
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
pt2a_total = 0

with open("aoc1.txt", "rt") as f:
    for line in f:
        # part 1
        digits = [c for c in line if c in DIGITS]
        pt1_total += int(f"{digits[0]}{digits[-1]}")

        # part 2
        line = line.lower().strip()
        for word, digit in NUM_MAP.items():
            line = line.replace(word, digit)
        digits = [c for c in line if c in DIGITS]
        pt2_total += int(f"{digits[0]}{digits[-1]}")

        # part 2a
        # technically more robust, could handle triples or longer correctly, e.g. "nineightwone"
        line = line.lower().strip()
        digits = []
        for start in range(len(line)):
            if line[start:][0] in DIGITS:
                digits.append(line[start])
            else:
                for word, digit in DIGIT_MAP.items():
                    if line[start:].startswith(word):
                        digits.append(digit)
        pt2a_total += int(f"{digits[0]}{digits[-1]}")


print(f"Part 1: {pt1_total}")
print(f"Part 2: {pt2_total}")
print(f"Part 2a: {pt2a_total}")
