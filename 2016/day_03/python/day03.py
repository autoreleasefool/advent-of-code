from aoc import AOC


aoc = AOC(year=2016, day=3)
data = aoc.load()


## Part 1

possibilities = 0
for line in data.lines():
    sides = line.split()
    possible = int(sides[0]) + int(sides[1]) > int(sides[2])
    possible = int(sides[1]) + int(sides[2]) > int(sides[0]) and possible
    possible = int(sides[0]) + int(sides[2]) > int(sides[1]) and possible
    if possible:
        possibilities += 1

aoc.p1(possibilities)


## Part 2

possibilities = 0
triangles = [[], [], []]
for line in data.lines():
    side = line.split()
    for i, _ in enumerate(side):
        triangles[i].append(side[i])
        if len(triangles[i]) == 3:
            possible = int(triangles[i][0]) + int(triangles[i][1]) > int(
                triangles[i][2]
            )
            possible = (
                int(triangles[i][1]) + int(triangles[i][2]) > int(triangles[i][0])
                and possible
            )
            possible = (
                int(triangles[i][0]) + int(triangles[i][2]) > int(triangles[i][1])
                and possible
            )
            triangles[i] = []
            if possible:
                possibilities += 1

aoc.p2(possibilities)
