from itertools import pairwise, groupby

PT1_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


# from itertools recipes
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def calculate_tail(nums):
    while True:
        if all_equal(nums):
            tails.append(nums[-1])
            break
        else:
            tails.append(nums[-1])
            nums = [(b - a) for (a, b) in pairwise(nums)]
    return sum(tails)

def calculate_head(nums):
    while True:
        if all_equal(nums):
            heads.append(nums[0])
            break
        else:
            heads.append(nums[0])
            nums = [(b - a) for (a, b) in pairwise(nums)]
    t = heads[-1]
    for x in reversed(heads[0:-1]):
        t = x - t
    return t


with open("aoc-input9.txt", "rt") as f:
    input = f.read().splitlines()
    #input = PT1_INPUT.splitlines()

total = 0
for line in input:
    tails = []
    nums = [int(x) for x in line.split()]
    total += calculate_tail(nums)

print(f"Part 1: {total}")

total = 0
for line in input:
    heads = []
    nums = [int(x) for x in line.split()]
    total += calculate_head(nums)
    print(nums)
    print(total)

print(f"Part 2: {total}")
