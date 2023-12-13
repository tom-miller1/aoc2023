from collections import defaultdict

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def count_matches(line):
    line = line[line.find(":")+1:]
    have, win = line.split("|")
    have = set(have.strip().split())
    win = set(win.strip().split())
    matches = have & win
    return len(matches)
    

def calculate_points(line):
    matches = count_matches(line)
    if matches > 0:
        points = 2**(matches - 1)
    else:
        points = 0

    return points


with open("input-day4.txt", "rt") as f:
    data = f.read()

    # part 1
    points = 0
    for line in data.splitlines():
        points += calculate_points(line)
    print(points)

    # part 2
    card_counts = defaultdict(int)
    for card, line in enumerate(data.splitlines(), start=1):
        card_counts[card] += 1
        new_copies = count_matches(line)
        if new_copies > 0:
            for card_num in range(card + 1, card + 1 + new_copies):
                card_counts[card_num] += card_counts[card]

    print(sum(card_counts.values()))

