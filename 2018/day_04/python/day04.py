from aoc import AOC
import re


aoc = AOC(year=2018, day=4)
data = aoc.load()


## Part 1

events = []
for line in data.lines():
    vals = [int(match) for match in re.findall(r"\d+", line)]
    if len(vals) == 5:
        year, month, day, hour, minute = vals
        guard_id = -1
    else:
        year, month, day, hour, minute, guard_id = vals
    text = line

    events.append((year, month, day, hour, minute, guard_id, text))

guards = {}
current_guard = 0
sleeping_starts = 0
events = sorted(events)
for event in events:
    year, month, day, hour, minute, guard_id, text = event
    if guard_id != -1:
        current_guard = guard_id

    if "asleep" in text:
        sleeping_starts = minute
    elif "wake" in text:
        if current_guard in guards:
            guards[current_guard] += minute - sleeping_starts
        else:
            guards[current_guard] = minute - sleeping_starts

max_mins = 0
max_id = 0
for guard in guards:
    if guards[guard] > max_mins:
        max_id = guard
        max_mins = guards[guard]

guard_id = max_id
minutes = {}
current_guard = -1
sleeping_starts = 0
for event in events:
    year, month, day, hour, minute, gid, text = event
    if gid != -1:
        current_guard = gid
    if current_guard != guard_id:
        continue

    if "asleep" in text:
        sleeping_starts = minute
    elif "wake" in text:
        for i in range(sleeping_starts, minute):
            if i in minutes:
                minutes[i] += 1
            else:
                minutes[i] = 1

max_minute = 0
max_count = 0
for minute in minutes:
    if minutes[minute] > max_count:
        max_count = minutes[minute]
        max_minute = minute

aoc.p1(guard_id * max_minute)


## Part 2


events = []
for line in data.lines():
    vals = [int(match) for match in re.findall(r"\d+", line)]
    if len(vals) == 5:
        year, month, day, hour, minute = vals
        gid = -1
    else:
        year, month, day, hour, minute, gid = vals
    text = line

    events.append((year, month, day, hour, minute, gid, text))

guards = {}
current_guard = 0
sleeping_starts = 0
events = sorted(events)
for event in events:
    year, month, day, hour, minute, gid, text = event
    if gid != -1:
        current_guard = gid

    if "asleep" in text:
        sleeping_starts = minute
    elif "wake" in text:
        if current_guard in guards:
            guards[current_guard] += minute - sleeping_starts
        else:
            guards[current_guard] = minute - sleeping_starts

minutes = {}
current_guard = -1
sleeping_starts = 0
for event in events:
    year, month, day, hour, minute, gid, text = event
    if gid != -1:
        current_guard = gid

    if "asleep" in text:
        sleeping_starts = minute
    elif "wake" in text:
        for i in range(sleeping_starts, minute):
            key = (current_guard, i)
            if key in minutes:
                minutes[key] += 1
            else:
                minutes[key] = 1

highest_minute = 0
best = None
for key in minutes:
    if minutes[key] > highest_minute:
        highest_minute = minutes[key]
        best = key

aoc.p2(best[0] * best[1])
