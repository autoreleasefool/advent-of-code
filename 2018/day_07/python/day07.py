from aoc import AOC
import re


aoc = AOC(year=2018, day=7)
data = aoc.load()


## Part 1


class Step:
    def __init__(self, children, parents):
        self.children = children
        self.parents = parents

    def __repr__(self):
        return str(self.children) + " -- " + str(self.parents)


steps = {}

for line in data.lines():
    line_steps = [match[1] for match in re.findall(r"(S|s)tep (\w)", line)]
    parent_name = line_steps[0]
    child_name = line_steps[1]

    if parent_name in steps:
        steps[parent_name].children.add(child_name)
    else:
        steps[parent_name] = Step(set([child_name]), set())

    if child_name in steps:
        steps[child_name].parents.add(parent_name)
    else:
        steps[child_name] = Step(set(), set([parent_name]))

order = ""
total_steps = len(steps)
while len(order) < total_steps:
    first_available = None
    for step_name in steps:
        step = steps[step_name]
        if not step.parents:
            if first_available is None:
                first_available = step_name
            elif step_name < first_available:
                first_available = step_name
    order += first_available
    del steps[first_available]
    for step_name in steps:
        step = steps[step_name]
        if first_available in step.parents:
            step.parents.remove(first_available)

aoc.p1(order)


## Part 2


class Step:
    def __init__(self, children, parents):
        self.children = children
        self.parents = parents

    def __repr__(self):
        return str(self.children) + " -- " + str(self.parents)


steps = {}


def time_for_step(step):
    return ord(step) - ord("A") + 61


for line in data.lines():
    line_steps = [match[1] for match in re.findall(r"(S|s)tep (\w)", line)]
    parent_name = line_steps[0]
    child_name = line_steps[1]

    if parent_name in steps:
        steps[parent_name].children.add(child_name)
    else:
        steps[parent_name] = Step(set([child_name]), set())

    if child_name in steps:
        steps[child_name].parents.add(parent_name)
    else:
        steps[child_name] = Step(set(), set([parent_name]))

ticks = 0
workers = [None] * 5
time_remaining = {}
empty_workers = list(workers)


def next_available_job():
    available = []
    for step in steps:
        if not steps[step].parents and step not in time_remaining:
            available.append(step)
    available.sort()
    return available[0] if available else None


while steps:
    for i, _ in enumerate(workers):
        if workers[i] is not None:
            worker_job = workers[i]
            time_remaining[worker_job] -= 1
            if time_remaining[worker_job] == 0:
                workers[i] = None
                del time_remaining[worker_job]
                del steps[worker_job]
                for step_name in steps:
                    if worker_job in steps[step_name].parents:
                        steps[step_name].parents.remove(worker_job)

    for i, _ in enumerate(workers):
        if workers[i] is None:
            job = next_available_job()
            if job is not None:
                workers[i] = job
                time_remaining[job] = time_for_step(job)

    if workers != empty_workers:
        ticks += 1

aoc.p2(ticks)
