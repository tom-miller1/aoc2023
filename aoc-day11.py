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
    empty = []
    for (row_idx, row) in enumerate(grid):
        if len(set(row)) == 1:
            empty.append(row_idx)

    return empty

def manhattan(empty_rows, empty_cols, pair, factor=2):
    star1 = stars[pair[0]]
    star2 = stars[pair[1]]
    span_rows = [row for row in empty_rows if min(star1[0], star2[0]) < row < max(star1[0], star2[0])]
    span_cols = [col for col in empty_cols if min(star1[1], star2[1]) < col < max(star1[1], star2[1])]
    delta_x = abs(star1[0] - star2[0]) + (factor - 1) * len(span_rows)
    delta_y = abs(star1[1] - star2[1]) + (factor - 1) * len(span_cols)
    return delta_x + delta_y


with open("aoc-input11.txt", "rt") as f:
    input = f.read()
#input = PT1_TEST

starfield = []
stars = {}
star_count = 1
for (row_idx, row) in enumerate(input.splitlines()):
    chars = []
    for (col_idx, char) in enumerate(row):
        if char == "#":
            char = star_count
            stars[star_count] = (row_idx, col_idx)
            star_count += 1
        chars.append(char)
    starfield.append(chars)

starfield = np.array(starfield)
# expand empty rows and columns
empty_rows = expand(starfield)
empty_cols = expand(starfield.T)

#print(empty_rows, empty_cols)
#print(stars)

total_distance = 0
for pair in combinations(stars, 2):
    distance = manhattan(empty_rows, empty_cols, pair)
    total_distance += distance
print(f"Part 1: {total_distance}")

total_distance = 0
for pair in combinations(stars, 2):
    distance = manhattan(empty_rows, empty_cols, pair, 1000000)
    total_distance += distance

print(f"Part 2: {total_distance}")
