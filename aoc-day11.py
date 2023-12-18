import numpy as np
from itertools import combinations

PT1_TEST = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def expand(grid, factor=1):
    repeat_rows = []
    for (row_idx, row) in enumerate(grid):
        if len(set(row)) == 1:
            repeat_rows.append(row_idx)
    for row_idx in reversed(repeat_rows):
        print(f"Copying row {row_idx}")
        for _ in range(factor):
            grid = np.insert(grid, row_idx, grid[row_idx], axis=0)
    return grid

def manhattan(grid, pair):
    p1 = np.array(np.where(grid == str(pair[0])))
    p2 = np.array(np.where(grid == str(pair[1])))
    return np.sum(np.abs(p1 - p2))


with open("aoc-input11.txt", "rt") as f:
    input = f.read()
input = PT1_TEST

starfield = []
star_count = 0
for line in input.splitlines():
    chars = []
    for char in line:
        if char == "#":
            char = str(star_count)
            star_count += 1
        chars.append(char)
    starfield.append(chars)

base_starfield = np.array(starfield)
# expand empty rows and columns
starfield = base_starfield
starfield = expand(starfield)
starfield = np.transpose(expand(starfield.T))

total_distance = 0
for pair in combinations(range(star_count), 2):
    distance = manhattan(starfield, pair)
    total_distance += distance
    #print(f"Pair: {pair}, {distance}")
print(total_distance)

# pt 2
starfield = base_starfield
starfield = expand(starfield, 999999)
starfield = np.transpose(expand(starfield.T, 999999))
total_distance = 0
for pair in combinations(range(star_count), 2):
    distance = manhattan(starfield, pair)
    total_distance += distance
print(total_distance)