import numpy as np

PT1_TEST = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

dirs = {
    # row, col ordered indexes
    "N" : np.array([-1, 0]),
    "S" : np.array([1, 0]),
    "E" : np.array([0, 1]),
    "W" : np.array([0, -1]),
}

opp_dirs = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}

exits = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
    ".": (),
    "S": (),
}


def print_grid(grid):
    letter_to_box = str.maketrans("|-LJ7F", "│─└┘┐┌")
    for row in grid:
        print("".join(row).translate(letter_to_box))
    print()


with open("aoc-input10.txt", "rt") as f:
    input = f.read()
#input = PT1_TEST

grid = []
start_position = None
for (row_index, row) in enumerate(input.splitlines()):
    s_index = row.find("S")
    if s_index != -1:
        start_position = np.array([row_index, s_index])
    grid.append(list(row.strip()))
grid = np.array(grid)

print_grid(grid)
print(start_position)

# travel around the loop and count how many cells get visited on the way back to S
visited = []
current_position = start_position
# find the first valid move from start
next_move = None
for direction in ["N", "S", "E", "W"]:
    check_position = start_position + dirs[direction]
    if opp_dirs[direction] in exits[grid[tuple(check_position)]]:
        next_move = direction
        break

next_pipe = None
while next_pipe != "S":
    current_position = current_position + dirs[direction]
    visited.append(current_position)
    direction = [x for x in exits[grid[tuple(current_position)]] if x != opp_dirs[direction]][0]
    next_pipe = grid[tuple(current_position + dirs[direction])]
    print(current_position, direction)

path_length = len(visited) + 1
print(f"Part 1: {path_length}")

