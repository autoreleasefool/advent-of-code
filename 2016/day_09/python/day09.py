from aoc import AOC
import re

aoc = AOC(year=2016, day=9)
data = aoc.load()

## Part 1

re_markers = re.compile(r"\((\d+)x(\d+)\)")

total_length = len(data.contents())
skip_until = 0
for marker in re_markers.finditer(data.contents()):
    if marker.start() < skip_until:
        continue
    total_length -= len(marker.group(0))
    total_length += int(marker.group(1)) * (int(marker.group(2)) - 1)
    skip_until = marker.end() + int(marker.group(1))

aoc.p1(total_length)


## Part 2


re_markers = re.compile(r"\((\d+)x(\d+)\)")


def get_decompressed_length(text):
    length = 0
    skip_until = 0
    unused_text = text
    for marker in re_markers.finditer(text):
        if marker.start() < skip_until:
            continue

        unused_text = unused_text.replace(
            text[marker.start() : marker.end() + int(marker.group(1))], "", 1
        )

        repeated_length = int(marker.group(1))
        repetitions = int(marker.group(2))
        repeated_group = text[marker.end() : marker.end() + repeated_length]

        decompressed_length = get_decompressed_length(repeated_group)
        additional_length = decompressed_length * repetitions
        length += additional_length

        skip_until = marker.end() + int(marker.group(1))

    length += len(unused_text)
    return length


total_length = get_decompressed_length(data.contents())

aoc.p2(total_length)
