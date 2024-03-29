from aoc import AOC
import queue

aoc = AOC(year=2018, day=15)
data = aoc.load()


walls = set()
caverns = set()
goblins = {}
elves = {}
beings = {}

total_elves = 0
total_goblins = 0
max_width = 0
max_height = 0

for y, line in enumerate(data.lines()):
    line = line.strip()
    for x, c in enumerate(line):
        parsed_cell = (x, y)
        if c == "#":
            walls.add(parsed_cell)
        elif c == ".":
            caverns.add(parsed_cell)
        elif c == "G":
            gob_id = "G{}".format(total_goblins)
            goblins[gob_id] = {"id": gob_id, "attack": 3, "hp": 200, "x": x, "y": y}
            beings[parsed_cell] = gob_id
            total_goblins += 1
            caverns.add(parsed_cell)
        elif c == "E":
            elf_id = "E{}".format(total_elves)
            elves[elf_id] = {"id": elf_id, "attack": 3, "hp": 200, "x": x, "y": y}
            beings[parsed_cell] = elf_id
            total_elves += 1
            caverns.add(parsed_cell)

        if y == 0:
            max_width += 1
    max_height += 1


def reading_order(c1, c2):
    if c1[1] < c2[1]:
        return c1
    if c2[1] < c1[1]:
        return c2
    return c1 if c1[0] < c2[0] else c2


def neighbors(n):
    ns = []
    if n[1] > 0:
        pot = (n[0], n[1] - 1)
        if pot not in walls:
            ns.append(pot)
    if n[0] > 0:
        pot = (n[0] - 1, n[1])
        if pot not in walls:
            ns.append(pot)
    if n[0] < max_width - 1:
        pot = (n[0] + 1, n[1])
        if pot not in walls:
            ns.append(pot)
    if n[1] < max_height - 1:
        pot = (n[0], n[1] + 1)
        if pot not in walls:
            ns.append(pot)
    return ns


def bfs(cell, targets):
    targets = set(targets)
    q = queue.PriorityQueue()
    dist = {cell: 0}
    prev = {}

    q.put((0, 0, 0, cell))

    def build_path(cell):
        path = [cell]
        p = prev[cell]
        while p is not None:
            path.append(p)
            p = prev[p] if p in prev else None

        path.reverse()
        return path

    while not q.empty():
        n = q.get()[3]

        for ne in neighbors(n):
            if ne in prev:
                continue

            if ne in caverns and ne not in beings:
                alt = dist[n] + 1
                if ne not in dist or alt < dist[ne]:
                    dist[ne] = alt
                    prev[ne] = n
                    if ne in targets:
                        return build_path(ne)[1]
                    q.put((alt, ne[1], ne[0], ne))
    return None


def remove(removed):
    if removed["id"][0] == "G":
        del goblins[removed["id"]]
    else:
        del elves[removed["id"]]
    del beings[(removed["x"], removed["y"])]


def get_target(cell, friendly_type):
    enemies = []
    for n in neighbors(cell):
        if friendly_type == "E" and n in beings and beings[n][0] == "G":
            enemies.append((goblins[beings[n]], n))
        elif friendly_type == "G" and n in beings and beings[n][0] == "E":
            enemies.append((elves[beings[n]], n))
    target = None
    for e in enemies:
        if target is None:
            target = e
        elif e[0]["hp"] < target[0]["hp"]:
            target = e
        else:
            target_order = reading_order(target[1], e[1])
            if target_order != target[1]:
                target = e
    return target[0] if target else None


def get_target_spaces(enemies):
    spaces = []
    for enemy_id in enemies:
        enemy = enemies[enemy_id]
        enemy_cell = (enemy["x"], enemy["y"])
        adjacent = neighbors(enemy_cell)
        spaces.extend(adjacent)
    return spaces


fighting = True
current_round = 0


# print_status()
while fighting:
    order = sorted(list(beings.keys()), key=lambda x: (x[1], x[0]))

    for being_position in order:
        if being_position not in beings:
            continue
        being_id = beings[being_position]
        being_type = being_id[0]

        if (being_type == "E" and not goblins) or (being_type == "G" and not elves):
            fighting = False
            break
        being = elves[being_id] if being_type == "E" else goblins[being_id]

        # pylint: disable=unsupported-assignment-operation, unsubscriptable-object
        current_target = get_target(being_position, being_type)
        if current_target is not None:
            current_target["hp"] -= being["attack"]
            if current_target["hp"] <= 0:
                remove(current_target)
        else:
            open_spaces = get_target_spaces(elves if being_type == "G" else goblins)
            if open_spaces:
                next_space = bfs(being_position, open_spaces)
                if next_space:
                    del beings[being_position]
                    beings[next_space] = being_id
                    if being_type == "E":
                        elves[being_id]["x"] = next_space[0]
                        elves[being_id]["y"] = next_space[1]
                    else:
                        goblins[being_id]["x"] = next_space[0]
                        goblins[being_id]["y"] = next_space[1]
            if next_space:
                current_target = get_target(next_space, being_type)
                if current_target:
                    current_target["hp"] -= being["attack"]
                    if current_target["hp"] <= 0:
                        remove(current_target)
    current_round += 1

survivors = elves if elves else goblins
total_health = sum(survivors[s]["hp"] for s in survivors)
aoc.p1((current_round - 1) * total_health)


## Part 2


def run_sim(starting_attack):
    walls = set()
    caverns = set()
    goblins = {}
    elves = {}
    beings = {}

    total_elves = 0
    total_goblins = 0
    max_width = 0
    max_height = 0

    for y, line in enumerate(data.lines()):
        line = line.strip()
        for x, c in enumerate(line):
            cell = (x, y)
            if c == "#":
                walls.add(cell)
            elif c == ".":
                caverns.add(cell)
            elif c == "G":
                gob_id = "G{}".format(total_goblins)
                goblins[gob_id] = {"id": gob_id, "attack": 3, "hp": 200, "x": x, "y": y}
                beings[cell] = gob_id
                total_goblins += 1
                caverns.add(cell)
            elif c == "E":
                elf_id = "E{}".format(total_elves)
                elves[elf_id] = {
                    "id": elf_id,
                    "attack": starting_attack,
                    "hp": 200,
                    "x": x,
                    "y": y,
                }
                beings[cell] = elf_id
                total_elves += 1
                caverns.add(cell)

            if y == 0:
                max_width += 1
        max_height += 1

    def reading_order(c1, c2):
        if c1[1] < c2[1]:
            return c1
        if c2[1] < c1[1]:
            return c2
        return c1 if c1[0] < c2[0] else c2

    def neighbors(n):
        ns = []
        if n[1] > 0:
            pot = (n[0], n[1] - 1)
            if pot not in walls:
                ns.append(pot)
        if n[0] > 0:
            pot = (n[0] - 1, n[1])
            if pot not in walls:
                ns.append(pot)
        if n[0] < max_width - 1:
            pot = (n[0] + 1, n[1])
            if pot not in walls:
                ns.append(pot)
        if n[1] < max_height - 1:
            pot = (n[0], n[1] + 1)
            if pot not in walls:
                ns.append(pot)
        return ns

    def bfs(cell, targets):
        targets = set(targets)
        q = queue.PriorityQueue()
        dist = {cell: 0}
        prev = {}

        q.put((0, 0, 0, cell))

        def build_path(cell):
            path = [cell]
            p = prev[cell]
            while p is not None:
                path.append(p)
                p = prev[p] if p in prev else None

            path.reverse()
            return path

        while not q.empty():
            n = q.get()[3]

            for ne in neighbors(n):
                if ne in prev:
                    continue

                if ne in caverns and ne not in beings:
                    alt = dist[n] + 1
                    if ne not in dist or alt < dist[ne]:
                        dist[ne] = alt
                        prev[ne] = n
                        if ne in targets:
                            return build_path(ne)[1]
                        q.put((alt, ne[1], ne[0], ne))
        return None

    def remove(being):
        if being["id"][0] == "G":
            del goblins[being["id"]]
        else:
            del elves[being["id"]]
        del beings[(being["x"], being["y"])]

    def get_target(cell, being_type):
        enemies = []
        for n in neighbors(cell):
            if being_type == "E" and n in beings and beings[n][0] == "G":
                enemies.append((goblins[beings[n]], n))
            elif being_type == "G" and n in beings and beings[n][0] == "E":
                enemies.append((elves[beings[n]], n))
        target = None
        for e in enemies:
            if target is None:
                target = e
            elif e[0]["hp"] < target[0]["hp"]:
                target = e
            else:
                target_order = reading_order(target[1], e[1])
                if target_order != target[1]:
                    target = e
        return target[0] if target else None

    def get_target_spaces(enemies):
        spaces = []
        for enemy_id in enemies:
            enemy = enemies[enemy_id]
            enemy_cell = (enemy["x"], enemy["y"])
            adjacent = neighbors(enemy_cell)
            spaces.extend(adjacent)
        return spaces

    fighting = True
    current_round = 0

    while fighting:
        order = sorted(list(beings.keys()), key=lambda x: (x[1], x[0]))

        for being_position in order:
            if being_position not in beings:
                continue
            being_id = beings[being_position]
            being_type = being_id[0]

            if (being_type == "E" and not goblins) or (being_type == "G" and not elves):
                fighting = False
                break
            being = elves[being_id] if being_type == "E" else goblins[being_id]

            # pylint: disable=unsupported-assignment-operation, unsubscriptable-object
            target = get_target(being_position, being_type)
            if target is not None:
                target["hp"] -= being["attack"]
                if target["hp"] <= 0:
                    if target["id"][0] == "E":
                        return False
                    remove(target)
            else:
                open_spaces = get_target_spaces(elves if being_type == "G" else goblins)
                if open_spaces:
                    next_space = bfs(being_position, open_spaces)
                    if next_space:
                        del beings[being_position]
                        beings[next_space] = being_id
                        if being_type == "E":
                            elves[being_id]["x"] = next_space[0]
                            elves[being_id]["y"] = next_space[1]
                        else:
                            goblins[being_id]["x"] = next_space[0]
                            goblins[being_id]["y"] = next_space[1]
                if next_space:
                    target = get_target(next_space, being_type)
                    if target:
                        target["hp"] -= being["attack"]
                        if target["hp"] <= 0:
                            if target["id"][0] == "E":
                                return False
                            remove(target)
        current_round += 1

    survivors = elves if elves else goblins
    total_health = sum(survivors[s]["hp"] for s in survivors)
    return True


elf_died = True
attack = 4
while elf_died:
    elf_died = not run_sim(attack)
    if not elf_died:
        aoc.p2(attack)
        break
    attack += 1
