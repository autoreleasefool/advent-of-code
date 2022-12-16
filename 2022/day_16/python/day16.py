from aoc import AOC
from functools import lru_cache
from heapq import heappush, heappop
from typing import List, Dict, Set
from dataclasses import dataclass, field
import re

aoc = AOC(year=2022, day=16)
data = aoc.load()

data.test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

@dataclass
class Valve:
    label: str
    rate: int
    tunnels: List[str] = field(default_factory=list)

valves: Dict[str, Valve] = {}
closed = set()
for valve in data.lines():
    components = re.match(r'^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$', valve)
    label = components.group(1)
    rate = int(components.group(2))
    tunnels = components.group(3).split(', ')
    if rate > 0:
        closed.add(label)
    valves[label] = Valve(
        label=label,
        rate=rate,
        tunnels=tunnels
    )

@lru_cache
def find_path(start: str, dest: str):
    prev = {start: None}
    to_visit = [start]

    def backtrack():
        path = [dest]
        cur = prev[dest]
        dist = 0
        while cur is not None:
            path.append(cur)
            dist += 1
            cur = prev[cur]
        return list(reversed(path))

    while to_visit:
        pos = to_visit.pop(0)
        if pos == dest:
            return backtrack()
        for n in valves[pos].tunnels:
            if n not in prev:
                prev[n] = pos
                to_visit.append(n)
    return []

@dataclass
class State:
    you: str
    closed: Set[str]
    flow_rate: int
    minutes_remaining: int
    visited: List[str]
    def __lt__(self, other):
        return self.you < other.you

def potential(state: State):
    return (
        -state.flow_rate,
        -(sum((state.minutes_remaining - len(find_path(state.you, v)) - 2) * valves[v].rate for v in state.closed)) + state.flow_rate
        # -(sum((state.minutes_remaining - distances[state.you][v] - 1) * valves[v].rate for v in state.closed) + state.flow_rate),
        # -state.flow_rate,
        # -state.minutes_remaining,
    )

q = [(0, State('AA', closed, 0, 30, ['AA']))]
while q:
    pp, state = heappop(q)

    if state.minutes_remaining == 0 or not state.closed:
        # aoc.d(state)

        aoc.d(f'{pp}, {state}')
        aoc.d(q)
        break
        # continue

    # if state.you_travelling:
    #     updated = State(
    #         state.you_travelling[0],
    #         state.you_travelling[1:],
    #         state.closed,
    #         state.flow_rate,
    #         state.minutes_remaining - 1,
    #         state.visited[:] + [state.you_travelling[0]]
    #     )
    #     heappush(q, (potential(updated), updated))
    if state.you in state.closed:
        update_closed = set(state.closed)
        update_closed.remove(state.you)
        updated = State(
            state.you,
            update_closed,
            state.flow_rate + valves[state.you].rate * (state.minutes_remaining - 1),
            state.minutes_remaining - 1,
            state.visited[:] + [f'Open {state.you}']
        )
        heappush(q, (potential(updated), updated))
    else:
        if not state.closed:
            heappush(q, (potential(updated), updated))
        else:
            for dest in state.closed:
                path = find_path(state.you, dest)[1:]
                dist = len(path)
                updated = State(
                    dest,
                    state.closed,
                    state.flow_rate,
                    state.minutes_remaining - dist,
                    state.visited + path
                )
                heappush(q, (potential(updated), updated))
