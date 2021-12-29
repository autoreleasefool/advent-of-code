from aoc import AOC, griditer, Position

aoc = AOC(year=2021, day=20)
data = aoc.load()

algorithm = data.lines()[0]
input_image = data.lines()[2:]

def pixel(bits):
    bits = ["0" if b == "." else "1" for b in bits]
    return algorithm[int("".join(bits), 2)]

def enhance(image, iteration):
    xrange = range(len(image[0]))
    yrange = range(len(image))

    output = []
    for y in range(-1, len(image) + 1):
        output.append([])
        for x in range(-1, len(image[0]) + 1):
            position = Position(x, y)
            pixels = []
            for adj in position.adjacent(include_self=True):
                if adj.x in xrange and adj.y in yrange:
                    pixels.append(image[adj.y][adj.x])
                else:
                    pixels.append("." if iteration % 2 == 0 else "#")
            output[-1].append(pixel(pixels))
    return output

# Part 1

for i in range(2):
    input_image = enhance(input_image, i)

aoc.p1(sum(1 for x, y in griditer(input_image) if input_image[y][x] == "#"))

# Part 2

input_image = data.lines()[2:]
for i in range(50):
    input_image = enhance(input_image, i)

aoc.p2(sum(1 for x, y in griditer(input_image) if input_image[y][x] == "#"))
