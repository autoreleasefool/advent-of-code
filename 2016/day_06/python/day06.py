from aoc import AOC


aoc = AOC(year=2016, day=6)
data = aoc.load()


## Part 1

letter_freq = [{} for x in range(len(data.lines()[0]))]

# Get frequencies of each letter, for each column
for line in data.lines():
    for index, letter in enumerate(line):
        if bool(not letter or letter.isspace()):
            continue
        letter_freq[index][letter] = (
            1 if letter not in letter_freq[index] else letter_freq[index][letter] + 1
        )

# Iterate over each column's letter frequencies and find the most frequent
secret_word = ""
for column_freq in letter_freq:
    most_frequent_letter = ""
    most_frequent_occurrences = -1
    for letter in column_freq:
        if column_freq[letter] > most_frequent_occurrences:
            most_frequent_letter = letter
            most_frequent_occurrences = column_freq[letter]

    secret_word += most_frequent_letter

aoc.p1(secret_word)

## Part 2

letter_freq = [{} for x in range(len(data.lines()[0]))]

# Get frequencies of each letter, for each column
for line in data.lines():
    for index, letter in enumerate(line):
        if bool(not letter or letter.isspace()):
            continue
        letter_freq[index][letter] = (
            1 if letter not in letter_freq[index] else letter_freq[index][letter] + 1
        )

# Iterate over each column's letter frequencies and find the least frequent
secret_word = ""
for column_freq in letter_freq:
    least_frequent_letter = ""
    least_frequent_occurrences = -1
    for letter in column_freq:
        if (
            column_freq[letter] < least_frequent_occurrences
            or least_frequent_occurrences == -1
        ):
            least_frequent_letter = letter
            least_frequent_occurrences = column_freq[letter]

    secret_word += least_frequent_letter

aoc.p2(secret_word)
