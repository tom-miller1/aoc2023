from itertools import cycle
from math import lcm

PT1_INPUT1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

PT1_INPUT2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

PT2_INPUT1 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

with open("aoc-input8.txt", "rt") as f:
    input = f.read()

directions = None
map = {}
for line in input.splitlines():
    if not directions:
        directions = line.strip()
        continue

    if "=" in line:
        node, dest = line.split(" = ")
        #print(node, dest)
        dest_l, dest_r = dest[1:-1].split(", ")
        map[node] = {
            "L": dest_l,
            "R": dest_r,
        }

# part 1
current_node = "AAA"
steps = 0
pt1_directions = cycle(directions)
while current_node != "ZZZ":
    current_node = map[current_node][next(pt1_directions)]
    steps += 1
print(steps, current_node)

# part 2
ghosts = [x for x in map if x.endswith("A")]
print(ghosts)
cycles = []
for ghost in ghosts:
    ghost_directions = cycle(directions)
    steps = 0
    while not ghost.endswith("Z"):
        ghost = map[ghost][next(ghost_directions)]
        steps +=1
    cycles.append(steps)
print(cycles)
print(lcm(*cycles))



