from aoc import AOC
from functools import lru_cache
from itertools import product
from heapq import heappush, heappop
from typing import List, Dict, Set, Optional
from dataclasses import dataclass, field
import re

aoc = AOC(year=2022, day=16)
AOC.skip_real_input = True
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
    rate: int
    tunnels: List[str]

valves: Dict[str, Valve] = {}
targetable_valves = set()
for valve in data.lines():
    components = re.match(r'^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$', valve)
    label = components.group(1)
    rate = int(components.group(2))
    tunnels = components.group(3).split(', ')

    if rate > 0:
        targetable_valves.add(label)

    valves[label] = Valve(rate=rate, tunnels=tunnels)

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
class Explorer:
    position: str
    target: str
    history: List[str]

@dataclass
class State:
    you: Explorer
    elephant: Explorer
    closed_valves: Set[str]
    flow_rate: int
    minutes_remaining: int
    previous_states: List[int]
    def __lt__(self, other):
        return self.you.position < other.you.position

    def your_targets(self):
        return [self.you.target] if self.you.target else self.closed_valves

    def elephant_targets(self):
        return [self.elephant.target] if self.elephant.target else self.closed_valves

def potential(state: State):
    potential_flow_rate = state.flow_rate
    for valve in state.closed_valves:
        your_travel_time = len(find_path(state.you.position, valve))
        elephant_travel_time = len(find_path(state.elephant.position, valve))
        fastest = min(your_travel_time, elephant_travel_time)
        if state.minutes_remaining >= fastest:
            potential_flow_rate += (state.minutes_remaining - fastest) * valves[valve].rate
    return potential_flow_rate

def priority(state: State):
    return -potential(state)

def push_qualifying_state(q, state: State):
    if state.minutes_remaining >= 0 and (not best_solution or potential(state) >= best_solution.flow_rate):
        heappush(q, (priority(state), state))

def has_reachable_valves(state: State):
    return any(
        len(find_path(state.you.position, valve)) <= state.minutes_remaining or
            len(find_path(state.elephant.position, valve)) <= state.minutes_remaining
            for valve in state.closed_valves
    )

state_id = 1
best_solution: Optional[State] = None
q = [(0, State(
    you=Explorer(position='AA', target=None, history=['AA']),
    elephant=Explorer(position='AA', target=None, history=['AA']),
    closed_valves=targetable_valves,
    flow_rate=0,
    minutes_remaining=26,
    previous_states=[]
))]

while q:
    _, state = heappop(q)

    if not has_reachable_valves(state):
        if not best_solution or state.flow_rate > best_solution.flow_rate:
            best_solution = state
            aoc.d(state)
        continue

    for your_target, elephant_target in product(state.your_targets(), state.elephant_targets()):
        if your_target == elephant_target:
            continue

        your_path = find_path(state.you.position, your_target)[1:]
        elephant_path = find_path(state.elephant.position, elephant_target)[1:]

        your_travel_time = len(your_path)
        elephant_travel_time = len(elephant_path)

        your_flow_rate_contribution = elephant_flow_rate_contribution = 0
        your_closed_valve = elephant_closed_valve = None

        if your_travel_time <= elephant_travel_time:
            your_next_position = your_target
            your_next_target = None
            your_next_history = state.you.history + [your_path + [f'Open {your_target}']]
            your_flow_rate_contribution = (state.minutes_remaining - your_travel_time - 1) * valves[your_target].rate
            your_closed_valve = your_target
            minutes_subtracted = your_travel_time + 1

            if your_travel_time == elephant_travel_time - 1:
                elephant_next_position = elephant_target
                elephant_next_target = elephant_target
                elephant_next_history = state.elephant.history + elephant_path
            elif your_travel_time < elephant_travel_time:
                elephant_next_position = elephant_path[your_travel_time + 1]
                elephant_next_target = elephant_target
                elephant_next_history = state.elephant.history + elephant_path[:your_travel_time + 2]

        if elephant_travel_time <= your_travel_time:
            elephant_next_position = elephant_target
            elephant_next_target = None
            elephant_next_history = state.elephant.history + [elephant_path + [f'Open {elephant_target}']]
            elephant_flow_rate_contribution = (state.minutes_remaining - elephant_travel_time - 1) * valves[elephant_target].rate
            elephant_closed_valve = elephant_target
            minutes_subtracted = elephant_travel_time + 1

            if elephant_travel_time == your_travel_time - 1:
                your_next_position = your_target
                your_next_target = your_target
                your_next_history = state.you.history + your_path
            elif elephant_travel_time < your_travel_time:
                your_next_position = your_path[elephant_travel_time + 1]
                your_next_target = your_target
                your_next_history = state.you.history + your_path[:elephant_travel_time + 2]

        next_state = State(
            you=Explorer(position=your_next_position, target=your_next_target, history=your_next_history),
            elephant=Explorer(position=elephant_next_position, target=elephant_next_target, history=elephant_next_history),
            closed_valves=state.closed_valves - set([your_closed_valve, elephant_closed_valve]),
            flow_rate=state.flow_rate + your_flow_rate_contribution + elephant_flow_rate_contribution,
            minutes_remaining=state.minutes_remaining - minutes_subtracted,
            previous_states=state.previous_states + [state]
        )
        push_qualifying_state(q, next_state)

    # for your_dest, elephant_dest in product(state.your_dests(), state.elephant_dests()):
    #     if your_dest == elephant_dest:
    #         continue

    #     your_path = find_path(state.you, your_dest)[1:]
    #     elephant_path = find_path(state.elephant, elephant_dest)[1:]
    #     your_dist = len(your_path)
    #     elephant_dist = len(elephant_path)

    #     next_state = State(
    #         your_position,
    #         your_destination
    #     )

    #     if your_dist < elephant_dist:
    #         next_state = State(
    #             your_dest,
    #             None,
    #             elephant_path[]
    #         )

    #     if your_dist == 0:
    #         updated = State(
    #             your_dest,
    #             None,
    #             elephant_path[your_dist + 1],
    #             elephant_dest,
    #             state.closed - set([your_dest]),
    #             state.flow_rate + valves[your_dest].rate * (state.minutes_remaining - your_dist - 1),
    #             state.minutes_remaining - your_dist - 1,
    #             state.visited + [your_path + [f'Open {your_dest}']],
    #             state.elephant_visited + [elephant_path[:your_dist + 2]]
    #         )
    #     elif your_dist == elephant_dist - 1:
    #         # Player moves to and opens valve, elephant moves to destination
    #         updated = State(
    #             your_dest,
    #             None,
    #             elephant_dest,
    #             elephant_dest,
    #             state.closed - set([your_dest]),
    #             state.flow_rate + valves[your_dest].rate * (state.minutes_remaining - your_dist - 1),
    #             state.minutes_remaining - your_dist - 1,
    #             state.visited + [your_path + [f'Open {your_dest}']],
    #             state.elephant_visited + [elephant_path]
    #         )
    #     elif your_dist < elephant_dist:
    #         # Player moves to and opens valve, elephant moves partway to destination
    #         updated = State(
    #             your_dest,
    #             None,
    #             elephant_path[your_dist + 1],
    #             elephant_dest,
    #             state.closed - set([your_dest]),
    #             state.flow_rate + valves[your_dest].rate * (state.minutes_remaining - your_dist - 1),
    #             state.minutes_remaining - your_dist - 1,
    #             state.visited + [your_path + [f'Open {your_dest}']],
    #             state.elephant_visited + [elephant_path[:your_dist + 2]]
    #         )
    #     elif elephant_dist == your_dist - 1:
    #         # Elephant moves to and opens valve, you move to destination
    #         updated = State(
    #             your_dest,
    #             your_dest,
    #             elephant_dest,
    #             None,
    #             state.closed - set([elephant_dest]),
    #             state.flow_rate + valves[elephant_dest].rate * (state.minutes_remaining - elephant_dist - 1),
    #             state.minutes_remaining - elephant_dist - 1,
    #             state.visited + [your_path],
    #             state.elephant_visited + [elephant_path  + [f'Open {elephant_dest}']]
    #         )
    #     elif elephant_dist < your_dist:
    #         # Elephant moves to and opens valve, you move partway to destination
    #         updated = State(
    #             your_path[elephant_dist + 1],
    #             your_dest,
    #             elephant_dest,
    #             None,
    #             state.closed - set([elephant_dest]),
    #             state.flow_rate + valves[elephant_dest].rate * (state.minutes_remaining - elephant_dist - 1),
    #             state.minutes_remaining - elephant_dist - 1,
    #             state.visited + [your_path[:elephant_dist + 2]],
    #             state.elephant_visited + [elephant_path  + [f'Open {elephant_dest}']]
    #         )
    #     else:
    #         # You and elephant move to destination and open valves
    #         updated = State(
    #             your_dest,
    #             None,
    #             elephant_dest,
    #             None,
    #             state.closed - set([elephant_dest, your_dest]),
    #             state.flow_rate
    #                 + valves[elephant_dest].rate * (state.minutes_remaining - elephant_dist - 1)
    #                 + valves[your_dest].rate * (state.minutes_remaining - your_dist - 1),
    #             state.minutes_remaining - your_dist - 1,
    #             state.visited + [your_path + [f'Open {your_dest}']],
    #             state.elephant_visited + [elephant_path  + [f'Open {elephant_dest}']]
    #         )

    #     # path = find_path(state.you, dest)[1:]
    #     # dist = len(path)
    #     # updated = State(
    #     #     dest,
    #     #     state.closed - set([dest]),
    #     #     state.flow_rate + valves[dest].rate * (state.minutes_remaining - dist - 1),
    #     #     state.minutes_remaining - dist - 1,
    #     #     state.visited + path + [f'Open {dest}']
    #     # )
    #     push_qualifying_state(q, updated)

aoc.p1(best_solution)
