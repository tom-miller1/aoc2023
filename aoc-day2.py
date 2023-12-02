MAX_CUBES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# Part 1
with open("aoc-input2.txt", "rt") as f:
    game_id_sum = 0

    for line in f:
        game_possible = True

        game, draw_sets = line.strip().split(":")
        _, game_id = game.split()
        for draw_set in draw_sets.split(";"):
            for cubes in draw_set.split(","):
                count, color = cubes.split()
                if int(count) > MAX_CUBES[color]:
                    game_possible = False

        if game_possible:
            game_id_sum += int(game_id)

print(f"Part 1: {game_id_sum}")

# Part 2
with open("aoc-input2.txt", "rt") as f:
    power_sum = 0

    for line in f:
        cube_min = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game, draw_sets = line.strip().split(":")
        _, game_id = game.split()
        for draw_set in draw_sets.split(";"):
            for cubes in draw_set.split(","):
                count, color = cubes.split()
                cube_min[color] = max((cube_min[color], int(count)))
        power_sum += cube_min["red"]*cube_min["green"]*cube_min["blue"]

print(f"Part 2: {power_sum}")