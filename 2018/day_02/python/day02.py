from aoc import AOC


aoc = AOC(year=2018, day=2)
data = aoc.load()

## Part 1

ids_with_pairs = set()
ids_with_triplets = set()

for box_id in data.lines():
    id_letters = {}
    for letter in box_id:
        if letter in id_letters:
            id_letters[letter] += 1
        else:
            id_letters[letter] = 1

    for letter in id_letters:
        if id_letters[letter] == 2:
            ids_with_pairs.add(box_id)
        if id_letters[letter] == 3:
            ids_with_triplets.add(box_id)

aoc.p1(len(ids_with_pairs) * len(ids_with_triplets))


## Part 2

ids_with_pairs = set()
ids_with_triplets = set()
ids = []


def solve_p2():
    for primary_box_id in data.lines():
        for secondary_box_id in data.lines():
            if primary_box_id == secondary_box_id:
                continue
            for i in range(len(primary_box_id)):
                adjusted_primary = primary_box_id[0:i] + primary_box_id[i + 1 :]
                adjusted_secondary = secondary_box_id[0:i] + secondary_box_id[i + 1 :]
                if adjusted_primary == adjusted_secondary:
                    aoc.p2(adjusted_primary)
                    return


solve_p2()
