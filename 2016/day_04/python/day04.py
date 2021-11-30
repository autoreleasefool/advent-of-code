from aoc import AOC
import operator

aoc = AOC(year=2016, day=4)
data = aoc.load()


## Part 1


def get_most_common(freq):
    # Returns the 5 most common letters, sorted by frequency, and alphabetically
    frequencies = []

    # Add letter, freq as tuple to list
    # Use negative frequency to sort in descending order
    for l in freq:
        frequencies.append((l, -freq[l]))

    frequencies = sorted(frequencies, key=operator.itemgetter(1, 0))
    return "".join([x[0] for x in frequencies[:5]])


sector_id_sum = 0
for line in data.lines():
    sectors = line.split("-")
    letter_freq = {}
    for sector_idx, _ in enumerate(sectors):
        if sector_idx < len(sectors) - 1:
            # Count frequency of each letter
            for letter in sectors[sector_idx]:
                if letter in letter_freq:
                    letter_freq[letter] += 1
                else:
                    letter_freq[letter] = 1
        else:
            # Compare checksum to 5 most common letters and add id to sum if equal
            checksum_start = sectors[sector_idx].index("[")
            checksum = sectors[sector_idx][checksum_start + 1 : checksum_start + 6]
            if checksum == get_most_common(letter_freq):
                sector_id_sum += int(sectors[sector_idx][:checksum_start])


aoc.p1(sector_id_sum)


## Part 2


def get_most_common(freq):
    # Returns the 5 most common letters, sorted by frequency, and alphabetically
    frequencies = []

    # Add letter, freq as tuple to list
    # Use negative frequency to sort in descending order
    for l in freq:
        frequencies.append((l, -freq[l]))

    frequencies = sorted(frequencies, key=operator.itemgetter(1, 0))
    return "".join([x[0] for x in frequencies[:5]])


def decrypt_name(start, sectors):
    # Rotate each letter in a sector name until the real name is found
    name = ""
    rotator_dist = int(sectors[len(sectors) - 1][:start])
    for idx, _ in enumerate(sectors):
        if idx == len(sectors) - 1:
            continue
        for l in sectors[idx]:
            actual_letter = chr(((ord(l) - ord("a") + rotator_dist) % 26) + ord("a"))
            name += actual_letter
    return name


for line in data.lines():
    base_sectors = line.split("-")
    letter_freq = {}
    for sector_idx, _ in enumerate(base_sectors):
        if sector_idx < len(base_sectors) - 1:
            # Count frequency of each letter
            for letter in base_sectors[sector_idx]:
                if letter in letter_freq:
                    letter_freq[letter] += 1
                else:
                    letter_freq[letter] = 1
        else:
            # Compare checksum to 5 most common letters and add id to sum if equal
            checksum_start = base_sectors[sector_idx].index("[")
            sector_id = base_sectors[len(base_sectors) - 1][:checksum_start]
            checksum = base_sectors[sector_idx][checksum_start + 1 : checksum_start + 6]
            if checksum == get_most_common(letter_freq):
                sector_name = decrypt_name(checksum_start, base_sectors)
                if sector_name == "northpoleobjectstorage":
                    # Print where the north pole objects are stored
                    aoc.p2(sector_id)
                    break
