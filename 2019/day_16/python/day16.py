from aoc import AOC


aoc = AOC(year=2019, day=16)
data = aoc.load()

base_pattern = [0, 1, 0, -1]
pattern = base_pattern

input_signal = [int(s) for s in data.contents()]

for _ in range(100):
    for el, _ in enumerate(input_signal):
        pattern = [value for value in base_pattern for i in range(el + 1)]
        input_signal[el] = (
            abs(
                sum(
                    [
                        val * pattern[(dig + 1) % len(pattern)]
                        for dig, val in enumerate(input_signal)
                    ]
                )
            )
            % 10
        )

aoc.p1("".join([str(s) for s in input_signal[:8]]))
